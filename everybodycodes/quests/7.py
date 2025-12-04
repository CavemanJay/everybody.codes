from enum import IntFlag
import timeit
from itertools import accumulate, cycle, groupby, islice, permutations
from math import factorial
from pprint import pprint
from typing import Callable
from icecream import ic
from ..utils import get_notes, loop, print_aligned, transpose

VALID_ACTION_PLAN = "+-=+-=+-=++"


def gen_action_plans():
    max_perms = factorial(11) // (factorial(5) * factorial(3) * factorial(3))
    count = 0

    chars = sorted(VALID_ACTION_PLAN)
    for p, _ in groupby(permutations(chars)):
        yield "".join(p)
        count += 1
        if count == max_perms:
            return


def unwind_track(t: str) -> str:
    lines = t.splitlines()
    grid = list(list(line) for line in lines)
    max_cols = max(len(row) for row in grid)
    for r in grid:
        if len(r) == max_cols:
            continue
        r += [" "] * (max_cols - len(r))
    total_rows = len(grid)
    total_cols = len(grid[0])
    row, col = 0, 1
    dx, dy = 1, 0  # dx positive = right, dy positive = down

    def change_direction():
        nonlocal dx, dy

        class Neighbors(IntFlag):
            TOP = 1 << 0
            RIGHT = 1 << 1
            BOTTOM = 1 << 2
            LEFT = 1 << 3
            ALL = TOP | RIGHT | BOTTOM | LEFT

        to_check = Neighbors.ALL
        # Don't check in the direction we are coming from
        if dx > 0:
            to_check = to_check & ~Neighbors.LEFT
        elif dx < 0:
            to_check = to_check & ~Neighbors.RIGHT
        elif dy > 0:
            to_check = to_check & ~Neighbors.TOP
        elif dy < 0:
            to_check = to_check & ~Neighbors.BOTTOM

        # Don't check beyond track bounds
        if col == total_cols - 1:
            to_check = to_check & ~Neighbors.RIGHT
        if col == 0:
            to_check = to_check & ~Neighbors.LEFT
        if row == total_rows - 1:
            to_check = to_check & ~Neighbors.BOTTOM
        if row == 0:
            to_check = to_check & ~Neighbors.TOP

        if to_check & Neighbors.BOTTOM:
            if grid[row + 1][col] != " ":
                dx, dy = 0, 1
                return

        if to_check & Neighbors.TOP:
            if grid[row - 1][col] != " ":
                dx, dy = 0, -1
                return

        if to_check & Neighbors.RIGHT:
            if grid[row][col + 1] != " ":
                dx, dy = 1, 0
                return

        if to_check & Neighbors.LEFT:
            if grid[row][col - 1] != " ":
                dx, dy = -1, 0
                return

    track = ""
    while not (row == 0 and col == 0):
        # if col == 70:
        #     breakpoint()
        current = grid[row][col]
        track += current
        if dx > 0:
            if col == total_cols - 1 or grid[row][col + 1] == " ":
                change_direction()
        elif dx < 0:
            if col == 0 or grid[row][col - 1] == " ":
                change_direction()
        elif dy > 0:
            if row == total_rows - 1 or grid[row + 1][col] == " ":
                change_direction()
        elif dy < 0:
            if row == 0 or grid[row - 1][col] == " ":
                change_direction()
        row += dy
        col += dx

    return track + "="


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
    rankings = (
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


def part_one(s: str):
    track = "=" * 10
    rankings = scores(s, track)
    return "".join(x[0] for x in sorted(rankings, key=lambda x: x[1], reverse=True))


def part_two(s: str):
    track = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""
    track = unwind_track(track)
    rankings = scores(s, track, 10)
    return "".join(x[0] for x in sorted(rankings, key=lambda x: x[1], reverse=True))


def part_three(track: str):
    track = unwind_track(track)
    plans = gen_action_plans()
    devicify = lambda plan: f"{plan}:{",".join(plan)}"
    loops = 1
    # rankings = [next(scores(devicify(plan), track, loops)) for plan in plans]
    # rankings = sorted(rankings, key=lambda r: r[1], reverse=True)
    # top = list(r for r in rankings if r[1] == rankings[0][1])
    rankings = []
    for plan in plans:
        rankings.append(next(scores(devicify(plan), track, loops)))
    rankings = sorted(rankings, key=lambda r: r[1], reverse=True)
    return 0


ex = """A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+"""

ex_track = """S+===
-   +
=+=-+"""


# ic(part_one(get_notes(1)))
# ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))
