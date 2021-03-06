r"""Assess the learning cost associated with the introduction of the given programs.

Each program has been previously found to implement a number of notions represented by a list of
taxons of the form: \(\textrm{segment}_0/\textrm{segment}_1/.../\textrm{segment}_n\), e.g.,
`flow/loop/exit/early/break`.

Furthermore, the notions already imparted may cover a certain **prefix** of such a taxon, e.g.
`flow/loop`. The learning cost should therefore not take it into account.

The cost of the remaining segments, here `exit/early/break`, is approximated by a function taking
two zero-based indexes `start` (inclusive) and `stop` (exclusive), and returning a floating number. Currently, only two such functions are provided:

1. `range_to_cost_linear()`, which simply counts the number of segments;
2. `range_to_cost_zeno()`, which calculates the sum of a decreasing function of the positions
   (with the assumption that the introduction of a sub-concept costs half that of its parent concept).
"""

from functools import lru_cache

from .user_types import TaxonName, TaxonNameSet, ProgramTaxonNames, AssessedPrograms, Literal

__pdoc__ = {
    "LearningCostAssessor.__call__": True,
}


@lru_cache(maxsize=None)  # NB: memoization needed for consistency with mypy's typing
def range_to_cost_linear(start: int, stop: int) -> float:
    """Return the length of the slice between `start` (inclusive) and `stop` (exclusive).
    """
    return float(stop - start)


@lru_cache(maxsize=None)
def range_to_cost_zeno(start: int, stop: int) -> float:
    r"""Calculate the sum of the given slice of a [Zeno's geometric series](https://en.wikipedia.org/wiki/Zeno%27s_paradoxes#Dichotomy_paradox).

    Specifically: $$\sum_{i=\textrm{start}}^{\textrm{stop}-1}{\frac{1}{2^{i+1}}}$$

    Since it converges absolutely towards 1, the returned value is in the interval \([0, 1[\).

    <center><a title="Jim.belk / Public domain" href="https://commons.wikimedia.org/wiki/File:Geometric_Segment.svg"><img width="256" alt="Geometric Segment" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Geometric_Segment.svg/256px-Geometric_Segment.svg.png"></a></center>

    Example:
        If `flow/loop` is already imparted, the learning cost of `flow/loop/exit/early/break` will
        be:

    >>> range_to_cost_zeno(2, 5)
    0.21875

    Indeed,
    \(\frac{1}{2^3}+\frac{1}{2^4}+\frac{1}{2^5}=\frac{1}{8}+\frac{1}{16}+\frac{1}{32}=0.21875\).

    """
    return sum(2 ** ~i for i in range(start, stop))


class LearningCostAssessor:
    def __init__(self, imparted_knowledge: TaxonNameSet) -> None:
        """Evaluate the learning costs of programs with respect to the given imparted knowledge.

        Args:
            imparted_knowledge (TaxonNameSet): A set of taxon names, representing all the notions
                introduced so far.
        """
        self.imparted_knowledge = imparted_knowledge

    def set_cost_assessment_strategy(self, strategy: Literal["zeno", "linear"] = "zeno") -> None:
        """Set the function to be used for the learning cost calculation.

        Args:
            strategy (str, optional): Either:

                - `"zeno"`: `range_to_cost_zeno` (default).
                - `"linear"`: `range_to_cost_linear`.

        Raises:
            NotImplementedError: Raised in case of unknown strategy.
        """
        if strategy.lower() == "zeno":
            self.range_to_cost = range_to_cost_zeno
        elif strategy == "linear":
            self.range_to_cost = range_to_cost_linear
        else:
            raise NotImplementedError
        self.range_to_cost.cache_clear()
        self.taxon_cost.cache_clear()

    @lru_cache(maxsize=None)
    def taxon_cost(self, taxon: TaxonName) -> float:
        """Evaluate the learning cost of a given taxon.

        The bounds of the not-yet-imparted suffix of the taxon are extracted and passed to the cost
        assessment function.

        Args:
            taxon (TaxonName): The taxon to be costed.

        Returns:
            float: The learning cost of the taxon.

        .. note::
          The learning cost of a taxon prefixed by `"metadata/"` is assumed to be zero.
        """
        if taxon.startswith("metadata/"):
            return 0
        (start, stop) = (0, 0)
        if taxon not in self.imparted_knowledge:
            segments = taxon.split("/")
            stop = len(segments)
            for start in range(stop - 1, -1, -1):
                if "/".join(segments[:start]) in self.imparted_knowledge:
                    break
        return self.range_to_cost(start, stop)

    def __call__(self, programs: ProgramTaxonNames) -> AssessedPrograms:
        """Associate the given programs with the total learning cost of their taxons.

        Args:
            programs (ProgramTaxonNames): A dictionary associating each program name with a list
                of taxon names.

        Returns:
            AssessedPrograms: A list of tuples `(total_cost, ProgramName)` sorted by increasing cost.
        """
        return sorted(
            (sum(map(self.taxon_cost, taxon_names)), program_name)
            for (program_name, taxon_names) in programs.items()
        )
