from collections import defaultdict

import pytest
import regex  # type: ignore
import sqlparse

import context
from make_snapshot import make_snapshot
from paroxython.generate_programs import generate_programs
from paroxython.parse_program import ProgramParser, find_all_features
from paroxython.preprocess_source import (
    centrifugate_hints,
    cleanup_factory,
    collect_hints,
    remove_hints,
)
from paroxython.title_to_slug import title_converter
from paroxython.user_types import Program


title_to_slug = title_converter()


def generate_toc(text):
    for match in regex.finditer(r"(?m)^(#{1,4}) (.+)", text):
        (hashtags, title) = match.groups()
        offset = "  " * (len(hashtags) - 1) + "- "
        slug = title_to_slug(title, deduplicate=True)
        yield f"{offset}[{title}](#{slug})"


def reformat_sql(match):
    s = sqlparse.format(
        match.group(1),
        reindent=True,
        keyword_case="upper",  # Limitation: https://github.com/andialbrecht/sqlparse/pull/501
        identifier_case="lower",
        indent_width=2,
    )
    s = s.replace("\n\n", "\n")
    s = regex.sub(r"\b(regexp|glob|inside)\b", lambda m: m.group().upper(), s)
    s = regex.sub(r"\b(PATH)\b", lambda m: m.group().lower(), s)
    return f"```sql\n{s}\n```"


def derivation_map(text):

    find_iter_derivations = regex.compile(
        r"""(?mx)
        name(_prefix)?\s(
            (=|==|REGEXP)\s"(?P<REQUIRED_LABEL_NAME>.+?)(:.*)?"
            |
            IN\s\(("(?P<REQUIRED_LABEL_NAME>.+?)(:.*)?"(.|\n)*?)+\)
            )
        |
        \b(FROM|JOIN)\st_(?P<REQUIRED_LABEL_NAME>\w+)
    """
    ).finditer

    def label_converter(label_patterns):
        cache = {}

        def label_name_to_pattern(label_name):
            if label_name not in cache:
                for label_pattern in label_patterns:
                    if regex.fullmatch(label_pattern, label_name):
                        cache[label_name] = label_pattern
                        break
                else:
                    raise ValueError(f"Unable to match '{label_name}' with a known pattern")
            return cache[label_name]

        return label_name_to_pattern

    derived_from = defaultdict(set)
    derived_into = defaultdict(set)
    all_features = find_all_features(text)
    label_name_to_pattern = label_converter([feature[0] for feature in all_features])
    for (label_pattern, language, query) in all_features:
        if language == "re":
            continue
        for m in find_iter_derivations(query):
            derived_label_patterns = [
                label_name_to_pattern(x) for x in m.captures("REQUIRED_LABEL_NAME")
            ]
            derived_from[label_pattern].update(derived_label_patterns)
            for derived_label_pattern in derived_label_patterns:
                derived_into[derived_label_pattern].add(label_pattern)
    keys = set(derived_from).union(derived_into)
    result = {}
    for key in keys:
        result[key] = {}
        if key in derived_from:
            result[key]["⬆️"] = sorted(derived_from[key])
        if key in derived_into:
            result[key]["⬇️"] = sorted(derived_into[key])
    return result


def inject_derivations(text):
    for (key, entries) in derivation_map(text).items():
        new_section = [f"##### Derivations\n"]
        for (kind, features) in entries.items():
            for feature in features:
                slug = title_to_slug(f"Feature `{feature}`")
                new_section.append(f"[{kind} feature `{feature}`](#{slug})  ")
        new_section.append("\n")
        text = regex.sub(
            r"(?msx)^(\#{4}\s+Feature\s+`%s`.+?)^(?=\#{5}\s+Specification)" % regex.escape(key),
            r"\1" + "\n".join(new_section),
            text,
        )
    return text


def reformat_file(feature_path):
    text = feature_path.read_text()
    toc = "\n".join(generate_toc(text))
    for m in regex.finditer(r"(?sm)^#### Feature (`.+?`).+?```(\w*)", text):
        if m[2] == "sql":
            toc = toc.replace(m[1], f"{m[1]} (SQL)")
    rule = "-" * 80 + "\n"
    text = regex.sub(r"(?m)^---+\n", "", text)
    text = regex.sub(r"(?m)^ +```", "```", text)
    text = regex.sub(r"(?ms).*?^(?=# )", fr"{toc}\n\n", text, count=1)
    text = regex.sub(r"(?m)\s+^(#+ .+)\s+", fr"\n\n\1\n\n", text)
    text = regex.sub(r"(?ms)^(\| Label \| .+?)(^\#{1,3} )", fr"\1{rule}\n\2", text)
    text = regex.sub(r"(?=\n\#{4} )", fr"\n{rule}", text)
    text = regex.sub(r"(?ms)^```sql\n(.+?)\n```", reformat_sql, text)
    text = regex.sub(r"(?ms)^\#{5} Derivations\n.+?^(?=\#{5} Specification)", "", text)
    text = inject_derivations(text)
    feature_path.write_text(text)


def extract_examples(feature_path):
    text = feature_path.read_text()
    rex = r"""(?msx)
        ^\#{4}\s+Feature\s+`(.+?)` # capture the label's pattern
        .+?\#{5}\s+Example # ensure the next code is in the Example section
        .+?```python\n+(.+?)\n``` # capture the source
        .+?\#{5}\s+Matches.+?^\|:--\|:--\| # ensure the table is in the Matches section
        (\n\|\s`(?P<LABELS>[^\|]+)`\s\|\s(?P<LINES>[^\|]+)\s\|)+ # capture the expected results
    """
    return regex.finditer(rex, text)


parse = ProgramParser()
reformat_file(parse.spec_path)
examples = []
for match in extract_examples(parse.spec_path):
    label_name = match.group(1)
    source = match.group(2)
    source = regex.sub(r"(?m)^.{1,4}", "", source)
    source = centrifugate_hints(source)
    (addition, deletion) = collect_hints(source)
    source = remove_hints(source)
    actual_results = dict(parse(Program(source=source, addition=addition, deletion=deletion)))
    expected_results = list(zip(match.captures("LABELS"), match.captures("LINES")))
    examples.append((label_name, actual_results, expected_results))


@pytest.mark.parametrize("label_name, actual_results, expected_results", examples)
def test_example(label_name, actual_results, expected_results):
    keys = set(actual_results.keys())
    print(actual_results)
    for (expected_label_name, expected_spans) in expected_results:
        assert expected_label_name in keys
        actual_spans = ", ".join(map(str, actual_results[expected_label_name]))
        assert actual_spans == expected_spans
        keys.discard(expected_label_name)
    for expected_label_name in keys:
        expected_name_prefix = expected_label_name.partition(":")[0]
        if regex.fullmatch(label_name, expected_name_prefix):
            actual_spans = ", ".join(map(str, actual_results[expected_label_name]))
            message = f"{expected_label_name} unexpectedly appears on {actual_spans}"
            raise AssertionError(message)


def test_at_least_one_example_is_provided_for_each_feature():
    expected = set(parse.features)
    actual_results = {label_name.partition(":")[0] for (label_name, _, _) in examples}
    assert actual_results.issuperset(expected)


def test_malformed_example():
    source = "if foo():\nbar() # wrong indentation"
    result = parse(Program(source=source))
    assert result == [("ast_construction:IndentationError", [])]


def test_label_presence(capsys):
    all_names = set()
    present_names = set()
    result = []
    for program in generate_programs("tests/data/simple/"):
        labels = parse(Program(source=program.source), yield_failed_matches=True)
        for (name, spans) in labels:
            all_names.add(name)
            if spans:
                present_names.add(name)
                result.append(name + f" / {program.path.name} / " + ", ".join(map(str, spans)))
    present = "\n- ".join(sorted(result))
    absent = "\n- ".join(sorted(all_names - present_names))
    text = f"# Present labels\n\n- {present}\n\n# Absent labels\n\n- {absent}\n"
    make_snapshot("snapshots/simple_labels.md", text, capsys)
