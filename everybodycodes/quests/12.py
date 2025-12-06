from collections import defaultdict
from itertools import count, islice
import itertools
import math
from pprint import pprint
import time
from icecream import ic
from line_profiler import profile
from ..utils import get_notes, print_aligned

coords = tuple[int, int]
Obj = tuple[coords, str]
Grid = list[list[str]]


def parse_map(s: str) -> tuple[list[Obj], list[Obj], Grid]:
    vals = list(
        ((r, c), char)
        for r, line in enumerate(s.splitlines())
        for c, char in enumerate(line)
        if char not in [".", "="]
    )
    target = ["T", "H"]

    return (
        [x for x in vals if x[1] not in target],
        [x for x in vals if x[1] in target],
        list(list(line) for line in s.splitlines()),
    )


def shoot(segment: Obj, target: Obj, grid: Grid):
    s, s_char = segment
    t, t_char = target

    x1, y1 = s[1], len(grid) - s[0] - 1
    x2, y2 = t[1], len(grid) - t[0] - 1
    for shot_power in count(1):
        max_height = y1 + shot_power
        distance = x1 + (shot_power * 2) + (max_height - 1)
        if distance < x2:
            continue
        if distance == x2 and y1 == y2:
            return shot_power
        assert distance >= x2
        distance_at_highest = x1 + shot_power * 2
        m = abs((max_height - y2) / (distance_at_highest - x2))
        if m == 1:
            return shot_power
        if m > 1:
            return None
    return None


def get_scores(s: str):
    segments, targets, grid = parse_map(s)
    scores: list[tuple[str, int, Obj]] = []
    while targets != []:
        target = targets.pop()
        for segment in segments:
            power_level = shoot(segment, target, grid)
            if power_level:
                scores.append(
                    (segment[1] * (2 if target[1] == "H" else 1), power_level, target)
                )
                # if target[1] == "H":
                #     grid[target[0][0]][target[0][1]] = "T"
                # elif target[1] == "T":
                grid[target[0][0]][target[0][1]] = "."
                break
        else:
            print("Not found")
    # print_aligned(grid)
    return scores


def part_one(s: str):
    return sum(
        (sum((ord(seg) - ord("A") + 1) for seg in segments) * score)
        for segments, score, _ in get_scores(s)
    )


part_two = part_one


ex1 = """
.............
.C...........
.B......T....
.A......T.T..
============="""[
    1:
]

ex2 = """
.............
.C...........
.B......H....
.A......T.H..
============="""[
    1:
]
ex3 = """
.C.................................................................................................
.B.................................................................................................
.A...............................................................................T.................
==================================================================================================="""[
    1:
]

# ic(part_one(ex1))
# ic(part_one(get_notes(1)))
# ic(part_two(ex2))
pprint(part_two(get_notes(2)))
# ic(get_scores(ex3))
