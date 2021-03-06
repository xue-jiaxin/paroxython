import json
from pathlib import Path

import pytest
import regex

import context
from make_snapshot import make_snapshot
from paroxython.label_programs import ProgramLabeller
from paroxython.user_types import Span, ProgramName


class ProgramEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type(ProgramName)):
            return str(obj)
        if isinstance(obj, Span):
            return obj.to_couple()
        if isinstance(obj, set):
            return sorted(obj)
        return json.JSONEncoder.default(self, obj)


labeller = ProgramLabeller()
labeller.label_programs(Path("tests/data/simple"))


def test_label_programs(capsys):
    result = labeller.programs
    text = json.dumps(result, cls=ProgramEncoder, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    make_snapshot(Path("tests/snapshots/simple_labelled_programs.json"), text, capsys)


def test_generate_labelled_sources(capsys):
    chunks = list(labeller.generate_labelled_sources())
    result = []
    for chunk in chunks:
        if chunk.startswith("#"):
            result.append(chunk)
        else:
            for line in chunk.split("\n"):
                if not line:
                    continue
                (source, _, comment) = line.partition(" # ")
                for label in comment.split(", "):
                    result.append(f"{source} # {label}")
                    source = " " * len(source)
            result.append("")
    make_snapshot(Path("tests/snapshots/simple_labelled_sources.py"), "\n".join(result), capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
