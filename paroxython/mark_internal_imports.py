from user_types import LabelName, ProgramName, ProgramNameSet, Programs


class InternalImportsMarker:
    def __init__(self, programs: Programs) -> None:
        self.all_program_names = {program.name for program in programs}

    def reset(self) -> None:
        self.internal_imports: ProgramNameSet = set()

    def __call__(self, label_name: LabelName) -> LabelName:
        """
        Return a modified copy of label "import:(module).*" when module.py belongs to the DB.

        As a side effect, store all these module.py program names in the set self.internal_imports.
        """
        if label_name.startswith(("import:", "import_module:")):
            parts = label_name.split(":")
            if f"{parts[1]}.py" in self.all_program_names:
                label_name = LabelName(f"{parts[0]}_internally:{':'.join(parts[1:])}")
                self.internal_imports.add(ProgramName(f"{parts[1]}.py"))
        return label_name
