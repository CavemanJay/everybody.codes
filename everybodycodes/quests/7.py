from itertools import accumulate, cycle, islice
from pprint import pprint
from typing import Callable
from icecream import ic
from ..utils import get_notes, loop, transpose


def unwind_track(t: str) -> str:
    lines = t.splitlines()
    grid = list(list(line) for line in lines)
    trans_grid = transpose(grid)
    top_row = grid[0][1::]
    right_col = trans_grid[-1][1:-1]
    bottom_row = grid[-1][::-1]
    left_col = trans_grid[0][1:-1] + ["="]
    return "".join(top_row + right_col + bottom_row + left_col)


def line_parser(n: int):
    def parse(s: str):
        name, ops = s.split(":")
        ops = ops.split(",")
        ops = loop(ops, n)
        return name, ops

    return parse


def scores(s: str, track: str, loops: int = 1):
    op_funcs: dict[str, Callable[[int], int]] = {
        "+": lambda x: x + 1,
        "=": lambda x: x,
        "-": lambda x: x - 1,
    }
    track = "".join(loop([track], loops))
    devices = map(line_parser(len(track)), s.splitlines())
    rankings = list(
        (
            device,
            sum(
                islice(
                    accumulate(
                        zip(ops, track),
                        lambda acc, op: (
                            op_funcs[op[0] if op[1] == "=" else op[1]](acc)
                        ),
                        initial=10,
                    ),
                    1,
                    None,
                )
            ),
        )
        for device, ops in devices
    )
    return rankings


def part_one(s: str, track: str):
    rankings = scores(s, track)
    return "".join(x[0] for x in sorted(rankings, key=lambda x: x[1], reverse=True))


def part_two(s: str, track: str):
    rankings = scores(s, track, 10)
    return "".join(x[0] for x in sorted(rankings, key=lambda x: x[1], reverse=True))


ex = """A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+"""

ex_track = """S+===
-   +
=+=-+"""

track = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""

# ic(part_one(ex, "=" * 10))
ic(part_one(get_notes(1), "=" * 10))
# ic(part_two(ex, unwind_track(ex_track)))
ic(part_two(get_notes(2), unwind_track(track)))
