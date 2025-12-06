from collections import defaultdict
from itertools import count, islice
import itertools
import math
import time
from icecream import ic
from line_profiler import profile
from ..utils import get_notes

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

    return (
        [x for x in vals if x[1] != "T"],
        [x for x in vals if x[1] == "T"],
        list(list(line) for line in s.splitlines()),
    )


@profile
def shoot(segment: Obj, target: Obj, grid: Grid):
    s, s_char = segment
    t, t_char = target

    # if s_char == "A":
    #     breakpoint()

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


@profile
def part_one(s: str):
    segments, targets, grid = parse_map(s)
    shot = set()
    scores: list[tuple[str, int, Obj]] = []
    for target in targets:
        for segment in segments:
            if target in shot:
                continue
            x = shoot(segment, target, grid)
            if x:
                shot.add(target)
                scores.append((segment[1], x, target))
    # return list((ord(seg) - ord("A") + 1)   for seg, score in scores)
    return sum(((ord(seg) - ord("A") + 1)* score) for seg, score, target in scores)


ex1 = """
.............
.C...........
.B......T....
.A......T.T..
============="""[
    1:
]

# ic(part_one(ex1))
ic(part_one(get_notes(1)))
