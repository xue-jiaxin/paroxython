import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter


db = json.loads(Path("tests/data/dummy/db.json").read_text())


def test_init():
    dbf = ProgramFilter(db)
    print(dbf.recommended_programs)
    assert dbf.recommended_programs.keys() == db["programs"].keys()
    assert not dbf.imparted_knowledge


def test_programs_of_taxons():
    dbf = ProgramFilter(db)
    taxons = {"X/S/M/L/R/D/A", "X/S/M/L/R/D", "non_existing_taxon"}
    programs = dbf.programs_of_taxons(taxons, follow_import=False)
    print(sorted(programs))
    for (db_program, db_program_data) in db["programs"].items():
        if taxons.intersection(db_program_data["taxons"]):
            assert db_program in programs
        else:
            assert db_program not in programs


def test_taxons_of_programs():
    dbf = ProgramFilter(db)
    programs = {"prg8.py", "prg9.py", "non_existing_program"}
    taxons = dbf.taxons_of_programs(programs)
    prg8_taxons = set(dbf.db_programs["prg8.py"]["taxons"])
    prg9_taxons = set(dbf.db_programs["prg9.py"]["taxons"])
    print(sorted(taxons))
    assert taxons == prg8_taxons | prg9_taxons


def test_patterns_to_taxons():
    dbf = ProgramFilter(db)
    patterns = ["X/S/M.*", "O(?!/C).*", "non_matching_pattern"]
    taxons = dbf.patterns_to_taxons(patterns)
    print(sorted(taxons))
    assert taxons == {
        "O",
        "O/J",
        "O/N",
        "O/N/P",
        "X/S/M",
        "X/S/M/L",
        "X/S/M/L/R",
        "X/S/M/L/R/D",
        "X/S/M/L/R/D/A",
        "X/S/M/L/V",
    }


def test_impart_taxons():
    dbf = ProgramFilter(db)
    taxons = ["O/J", "X/S/M/L", "non_existing_taxon"]
    dbf.impart_taxons(taxons)
    print(sorted(dbf.imparted_knowledge))
    assert dbf.imparted_knowledge == {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}


def test_exclude_taxons():
    dbf = ProgramFilter(db)
    taxons = ["O/J", "X/S/M/L", "non_existing_taxon"]
    dbf.exclude_taxons(taxons)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs.keys() == {"prg2.py", "prg5.py"}
    for taxon in taxons:
        assert taxon not in db["programs"]["prg2.py"]["taxons"]
        assert taxon not in db["programs"]["prg5.py"]["taxons"]


def test_include_taxons():
    dbf = ProgramFilter(db)
    taxons = ["O/J", "X/S/M/L", "non_existing_taxon"]
    dbf.include_taxons(taxons)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs.keys() == {
        "prg1.py",
        "prg3.py",
        "prg4.py",
        "prg6.py",
        "prg7.py",
        "prg8.py",
        "prg9.py",
    }


def test_patterns_to_programs():
    dbf = ProgramFilter(db)
    patterns = ["prg[1-3]", "prg[7-9]", "non_matching_pattern"]
    programs = dbf.patterns_to_programs(patterns)
    print(sorted(programs))
    assert programs == {"prg1.py", "prg2.py", "prg3.py", "prg7.py", "prg8.py", "prg9.py"}


def test_impart_programs():
    dbf = ProgramFilter(db)
    programs = {"prg1.py", "prg2.py", "non_existing_program"}
    dbf.impart_programs(programs)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs.keys() == set(db["programs"]) - set(programs)
    print(sorted(dbf.imparted_knowledge))
    assert set(db["taxons"]) - dbf.imparted_knowledge == {
        "O/C/F",
        "O/C/F/U",
        "X/S/M/L/R/D/A",
        "Y/E",
    }


def test_exclude_programs():
    dbf = ProgramFilter(db)
    programs = {"prg1.py", "prg2.py", "non_existing_program"}
    dbf.exclude_programs(programs)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs.keys() == set(db["programs"]) - set(programs)


def test_include_programs():
    dbf = ProgramFilter(db)
    programs = {"prg1.py", "prg2.py", "non_existing_program"}
    dbf.include_programs(programs)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs.keys() == {"prg1.py", "prg2.py"}
