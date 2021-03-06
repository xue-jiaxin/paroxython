# Generated by helpers/make_compare_spans.py on 2020-05-01 20:22:28.196856.
# Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.

compare_spans = {
    "x<x<y<y": lambda x, y: x[0] < x[1] < y[0] < y[1],
    "x<x<y≤y": lambda x, y: x[0] < x[1] < y[0] <= y[1],
    "x<x<y=y": lambda x, y: x[0] < x[1] < y[0] == y[1],
    "x<x≤y<y": lambda x, y: x[0] < x[1] <= y[0] < y[1],
    "x<x≤y≤y": lambda x, y: x[0] < x[1] <= y[0] <= y[1],
    "x<x≤y=y": lambda x, y: x[0] < x[1] <= y[0] == y[1],
    "x<x=y<y": lambda x, y: x[0] < x[1] == y[0] < y[1],
    "x<x=y≤y": lambda x, y: x[0] < x[1] == y[0] <= y[1],
    "x<x=y=y": lambda x, y: x[0] < x[1] == y[0] == y[1],
    "x≤x<y<y": lambda x, y: x[0] <= x[1] < y[0] < y[1],
    "x≤x<y≤y": lambda x, y: x[0] <= x[1] < y[0] <= y[1],
    "x≤x<y=y": lambda x, y: x[0] <= x[1] < y[0] == y[1],
    "x≤x≤y<y": lambda x, y: x[0] <= x[1] <= y[0] < y[1],
    "x≤x≤y≤y": lambda x, y: x[0] <= x[1] <= y[0] <= y[1],
    "x≤x≤y=y": lambda x, y: x[0] <= x[1] <= y[0] == y[1],
    "x≤x=y<y": lambda x, y: x[0] <= x[1] == y[0] < y[1],
    "x≤x=y≤y": lambda x, y: x[0] <= x[1] == y[0] <= y[1],
    "x≤x=y=y": lambda x, y: x[0] <= x[1] == y[0] == y[1],
    "x=x<y<y": lambda x, y: x[0] == x[1] < y[0] < y[1],
    "x=x<y≤y": lambda x, y: x[0] == x[1] < y[0] <= y[1],
    "x=x<y=y": lambda x, y: x[0] == x[1] < y[0] == y[1],
    "x=x≤y<y": lambda x, y: x[0] == x[1] <= y[0] < y[1],
    "x=x≤y≤y": lambda x, y: x[0] == x[1] <= y[0] <= y[1],
    "x=x≤y=y": lambda x, y: x[0] == x[1] <= y[0] == y[1],
    "x=x=y<y": lambda x, y: x[0] == x[1] == y[0] < y[1],
    "x=x=y≤y": lambda x, y: x[0] == x[1] == y[0] <= y[1],
    "x=x=y=y": lambda x, y: x[0] == x[1] == y[0] == y[1],
    "x<y<x<y": lambda x, y: x[0] < y[0] < x[1] < y[1],
    "x<y<x≤y": lambda x, y: x[0] < y[0] < x[1] <= y[1],
    "x<y<x=y": lambda x, y: x[0] < y[0] < x[1] == y[1],
    "x<y≤x<y": lambda x, y: x[0] < y[0] <= x[1] < y[1],
    "x<y≤x≤y": lambda x, y: x[0] < y[0] <= x[1] <= y[1],
    "x<y≤x=y": lambda x, y: x[0] < y[0] <= x[1] == y[1],
    "x<y=x<y": lambda x, y: x[0] < y[0] == x[1] < y[1],
    "x<y=x≤y": lambda x, y: x[0] < y[0] == x[1] <= y[1],
    "x<y=x=y": lambda x, y: x[0] < y[0] == x[1] == y[1],
    "x≤y<x<y": lambda x, y: x[0] <= y[0] < x[1] < y[1],
    "x≤y<x≤y": lambda x, y: x[0] <= y[0] < x[1] <= y[1],
    "x≤y<x=y": lambda x, y: x[0] <= y[0] < x[1] == y[1],
    "x≤y≤x<y": lambda x, y: x[0] <= y[0] <= x[1] < y[1],
    "x≤y≤x≤y": lambda x, y: x[0] <= y[0] <= x[1] <= y[1],
    "x≤y≤x=y": lambda x, y: x[0] <= y[0] <= x[1] == y[1],
    "x≤y=x<y": lambda x, y: x[0] <= y[0] == x[1] < y[1],
    "x≤y=x≤y": lambda x, y: x[0] <= y[0] == x[1] <= y[1],
    "x≤y=x=y": lambda x, y: x[0] <= y[0] == x[1] == y[1],
    "x=y<x<y": lambda x, y: x[0] == y[0] < x[1] < y[1],
    "x=y<x≤y": lambda x, y: x[0] == y[0] < x[1] <= y[1],
    "x=y<x=y": lambda x, y: x[0] == y[0] < x[1] == y[1],
    "x=y≤x<y": lambda x, y: x[0] == y[0] <= x[1] < y[1],
    "x=y≤x≤y": lambda x, y: x[0] == y[0] <= x[1] <= y[1],
    "x=y≤x=y": lambda x, y: x[0] == y[0] <= x[1] == y[1],
    "x=y=x<y": lambda x, y: x[0] == y[0] == x[1] < y[1],
    "x=y=x≤y": lambda x, y: x[0] == y[0] == x[1] <= y[1],
    "x=y=x=y": lambda x, y: x[0] == y[0] == x[1] == y[1],
    "x<y<y<x": lambda x, y: x[0] < y[0] < y[1] < x[1],
    "x<y<y≤x": lambda x, y: x[0] < y[0] < y[1] <= x[1],
    "x<y<y=x": lambda x, y: x[0] < y[0] < y[1] == x[1],
    "x<y≤y<x": lambda x, y: x[0] < y[0] <= y[1] < x[1],
    "x<y≤y≤x": lambda x, y: x[0] < y[0] <= y[1] <= x[1],
    "x<y≤y=x": lambda x, y: x[0] < y[0] <= y[1] == x[1],
    "x<y=y<x": lambda x, y: x[0] < y[0] == y[1] < x[1],
    "x<y=y≤x": lambda x, y: x[0] < y[0] == y[1] <= x[1],
    "x<y=y=x": lambda x, y: x[0] < y[0] == y[1] == x[1],
    "x≤y<y<x": lambda x, y: x[0] <= y[0] < y[1] < x[1],
    "x≤y<y≤x": lambda x, y: x[0] <= y[0] < y[1] <= x[1],
    "x≤y<y=x": lambda x, y: x[0] <= y[0] < y[1] == x[1],
    "x≤y≤y<x": lambda x, y: x[0] <= y[0] <= y[1] < x[1],
    "x≤y≤y≤x": lambda x, y: x[0] <= y[0] <= y[1] <= x[1],
    "x≤y≤y=x": lambda x, y: x[0] <= y[0] <= y[1] == x[1],
    "x≤y=y<x": lambda x, y: x[0] <= y[0] == y[1] < x[1],
    "x≤y=y≤x": lambda x, y: x[0] <= y[0] == y[1] <= x[1],
    "x≤y=y=x": lambda x, y: x[0] <= y[0] == y[1] == x[1],
    "x=y<y<x": lambda x, y: x[0] == y[0] < y[1] < x[1],
    "x=y<y≤x": lambda x, y: x[0] == y[0] < y[1] <= x[1],
    "x=y<y=x": lambda x, y: x[0] == y[0] < y[1] == x[1],
    "x=y≤y<x": lambda x, y: x[0] == y[0] <= y[1] < x[1],
    "x=y≤y≤x": lambda x, y: x[0] == y[0] <= y[1] <= x[1],
    "x=y≤y=x": lambda x, y: x[0] == y[0] <= y[1] == x[1],
    "x=y=y<x": lambda x, y: x[0] == y[0] == y[1] < x[1],
    "x=y=y≤x": lambda x, y: x[0] == y[0] == y[1] <= x[1],
    "x=y=y=x": lambda x, y: x[0] == y[0] == y[1] == x[1],
    "y<x<x<y": lambda x, y: y[0] < x[0] < x[1] < y[1],
    "y<x<x≤y": lambda x, y: y[0] < x[0] < x[1] <= y[1],
    "y<x<x=y": lambda x, y: y[0] < x[0] < x[1] == y[1],
    "y<x≤x<y": lambda x, y: y[0] < x[0] <= x[1] < y[1],
    "y<x≤x≤y": lambda x, y: y[0] < x[0] <= x[1] <= y[1],
    "y<x≤x=y": lambda x, y: y[0] < x[0] <= x[1] == y[1],
    "y<x=x<y": lambda x, y: y[0] < x[0] == x[1] < y[1],
    "y<x=x≤y": lambda x, y: y[0] < x[0] == x[1] <= y[1],
    "y<x=x=y": lambda x, y: y[0] < x[0] == x[1] == y[1],
    "y≤x<x<y": lambda x, y: y[0] <= x[0] < x[1] < y[1],
    "y≤x<x≤y": lambda x, y: y[0] <= x[0] < x[1] <= y[1],
    "y≤x<x=y": lambda x, y: y[0] <= x[0] < x[1] == y[1],
    "y≤x≤x<y": lambda x, y: y[0] <= x[0] <= x[1] < y[1],
    "y≤x≤x≤y": lambda x, y: y[0] <= x[0] <= x[1] <= y[1],
    "y≤x≤x=y": lambda x, y: y[0] <= x[0] <= x[1] == y[1],
    "y≤x=x<y": lambda x, y: y[0] <= x[0] == x[1] < y[1],
    "y≤x=x≤y": lambda x, y: y[0] <= x[0] == x[1] <= y[1],
    "y≤x=x=y": lambda x, y: y[0] <= x[0] == x[1] == y[1],
    "y=x<x<y": lambda x, y: y[0] == x[0] < x[1] < y[1],
    "y=x<x≤y": lambda x, y: y[0] == x[0] < x[1] <= y[1],
    "y=x<x=y": lambda x, y: y[0] == x[0] < x[1] == y[1],
    "y=x≤x<y": lambda x, y: y[0] == x[0] <= x[1] < y[1],
    "y=x≤x≤y": lambda x, y: y[0] == x[0] <= x[1] <= y[1],
    "y=x≤x=y": lambda x, y: y[0] == x[0] <= x[1] == y[1],
    "y=x=x<y": lambda x, y: y[0] == x[0] == x[1] < y[1],
    "y=x=x≤y": lambda x, y: y[0] == x[0] == x[1] <= y[1],
    "y=x=x=y": lambda x, y: y[0] == x[0] == x[1] == y[1],
    "y<x<y<x": lambda x, y: y[0] < x[0] < y[1] < x[1],
    "y<x<y≤x": lambda x, y: y[0] < x[0] < y[1] <= x[1],
    "y<x<y=x": lambda x, y: y[0] < x[0] < y[1] == x[1],
    "y<x≤y<x": lambda x, y: y[0] < x[0] <= y[1] < x[1],
    "y<x≤y≤x": lambda x, y: y[0] < x[0] <= y[1] <= x[1],
    "y<x≤y=x": lambda x, y: y[0] < x[0] <= y[1] == x[1],
    "y<x=y<x": lambda x, y: y[0] < x[0] == y[1] < x[1],
    "y<x=y≤x": lambda x, y: y[0] < x[0] == y[1] <= x[1],
    "y<x=y=x": lambda x, y: y[0] < x[0] == y[1] == x[1],
    "y≤x<y<x": lambda x, y: y[0] <= x[0] < y[1] < x[1],
    "y≤x<y≤x": lambda x, y: y[0] <= x[0] < y[1] <= x[1],
    "y≤x<y=x": lambda x, y: y[0] <= x[0] < y[1] == x[1],
    "y≤x≤y<x": lambda x, y: y[0] <= x[0] <= y[1] < x[1],
    "y≤x≤y≤x": lambda x, y: y[0] <= x[0] <= y[1] <= x[1],
    "y≤x≤y=x": lambda x, y: y[0] <= x[0] <= y[1] == x[1],
    "y≤x=y<x": lambda x, y: y[0] <= x[0] == y[1] < x[1],
    "y≤x=y≤x": lambda x, y: y[0] <= x[0] == y[1] <= x[1],
    "y≤x=y=x": lambda x, y: y[0] <= x[0] == y[1] == x[1],
    "y=x<y<x": lambda x, y: y[0] == x[0] < y[1] < x[1],
    "y=x<y≤x": lambda x, y: y[0] == x[0] < y[1] <= x[1],
    "y=x<y=x": lambda x, y: y[0] == x[0] < y[1] == x[1],
    "y=x≤y<x": lambda x, y: y[0] == x[0] <= y[1] < x[1],
    "y=x≤y≤x": lambda x, y: y[0] == x[0] <= y[1] <= x[1],
    "y=x≤y=x": lambda x, y: y[0] == x[0] <= y[1] == x[1],
    "y=x=y<x": lambda x, y: y[0] == x[0] == y[1] < x[1],
    "y=x=y≤x": lambda x, y: y[0] == x[0] == y[1] <= x[1],
    "y=x=y=x": lambda x, y: y[0] == x[0] == y[1] == x[1],
    "y<y<x<x": lambda x, y: y[0] < y[1] < x[0] < x[1],
    "y<y<x≤x": lambda x, y: y[0] < y[1] < x[0] <= x[1],
    "y<y<x=x": lambda x, y: y[0] < y[1] < x[0] == x[1],
    "y<y≤x<x": lambda x, y: y[0] < y[1] <= x[0] < x[1],
    "y<y≤x≤x": lambda x, y: y[0] < y[1] <= x[0] <= x[1],
    "y<y≤x=x": lambda x, y: y[0] < y[1] <= x[0] == x[1],
    "y<y=x<x": lambda x, y: y[0] < y[1] == x[0] < x[1],
    "y<y=x≤x": lambda x, y: y[0] < y[1] == x[0] <= x[1],
    "y<y=x=x": lambda x, y: y[0] < y[1] == x[0] == x[1],
    "y≤y<x<x": lambda x, y: y[0] <= y[1] < x[0] < x[1],
    "y≤y<x≤x": lambda x, y: y[0] <= y[1] < x[0] <= x[1],
    "y≤y<x=x": lambda x, y: y[0] <= y[1] < x[0] == x[1],
    "y≤y≤x<x": lambda x, y: y[0] <= y[1] <= x[0] < x[1],
    "y≤y≤x≤x": lambda x, y: y[0] <= y[1] <= x[0] <= x[1],
    "y≤y≤x=x": lambda x, y: y[0] <= y[1] <= x[0] == x[1],
    "y≤y=x<x": lambda x, y: y[0] <= y[1] == x[0] < x[1],
    "y≤y=x≤x": lambda x, y: y[0] <= y[1] == x[0] <= x[1],
    "y≤y=x=x": lambda x, y: y[0] <= y[1] == x[0] == x[1],
    "y=y<x<x": lambda x, y: y[0] == y[1] < x[0] < x[1],
    "y=y<x≤x": lambda x, y: y[0] == y[1] < x[0] <= x[1],
    "y=y<x=x": lambda x, y: y[0] == y[1] < x[0] == x[1],
    "y=y≤x<x": lambda x, y: y[0] == y[1] <= x[0] < x[1],
    "y=y≤x≤x": lambda x, y: y[0] == y[1] <= x[0] <= x[1],
    "y=y≤x=x": lambda x, y: y[0] == y[1] <= x[0] == x[1],
    "y=y=x<x": lambda x, y: y[0] == y[1] == x[0] < x[1],
    "y=y=x≤x": lambda x, y: y[0] == y[1] == x[0] <= x[1],
    "y=y=x=x": lambda x, y: y[0] == y[1] == x[0] == x[1],
}

# Translate the 13 Allen's interval algebra relations, with all inequalities regarded as inclusive.
#
# Cf. Fig. 4 of Allen, James F. (26 Nov. 1983). "Maintaining knowledge about temporal intervals".
# Communications of the ACM. 26 (11): 832–843. doi:10.1145/182.358434
# http://cse.unl.edu/~choueiry/Documents/Allen-CACM1983.pdf

compare_spans.update(
    {  #                                              Allen's symbols
        "before": compare_spans["x≤x≤y≤y"],  #             <
        "equal": compare_spans["x=y≤x=y"],  #              =
        "meets": compare_spans["x≤x=y≤y"],  #              m
        "overlaps": compare_spans["x≤y≤x≤y"],  #           o
        "during": compare_spans["y≤x≤x≤y"],  #             d
        "starts": compare_spans["x=y≤x≤y"],  #             s
        "finishes": compare_spans["y≤x≤x=y"],  #           f
        "after": compare_spans["y≤y≤x≤x"],  #              >
        "met by": compare_spans["y≤y=x≤x"],  #             mi
        "overlapped by": compare_spans["y≤x≤y≤x"],  #      oi
        "contains": compare_spans["x≤y≤y≤x"],  #           di
        "started by": compare_spans["y=x≤y≤x"],  #         si
        "finished by": compare_spans["x≤y≤y=x"],  #        fi
    }
)

# Add some extra synonyms.

compare_spans.update(
    {
        "inside": compare_spans["during"],
        "is": compare_spans["equal"],
        "equals": compare_spans["equal"],
        "is after": compare_spans["after"],
        "is before": compare_spans["before"],
    }
)
