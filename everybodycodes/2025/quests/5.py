from itertools import takewhile
from typing import Sequence
from icecream import ic
from functools import cmp_to_key
from everybodycodes.utils import get_notes

OptInt = int | None


def from_digits(l: Sequence[OptInt]):
    return int("".join(str(d) for d in l if d is not None))


def build_fishbone(s: str):
    id, nums = s.split(":")
    nums = [int(x) for x in nums.split(",")]
    levels: list[list[OptInt]] = []
    spine: list[int] = []

    for n in nums:
        if spine == []:
            spine.append(n)
            levels.append([None, n, None])
            continue
        for level in levels:
            assert level[1] != None
            if n < level[1] and level[0] == None:
                level[0] = n
                break
            elif n > level[1] and level[2] == None:
                level[2] = n
                break
        else:
            spine.append(n)
            levels.append([None, n, None])

    return int(id), levels, from_digits(spine)


def part_one(s: str):
    _, _, spine = build_fishbone(s)
    return spine


def part_two(s: str):
    bone_scores = [spine for _, _, spine in map(build_fishbone, s.splitlines())]
    return max(bone_scores) - min(bone_scores)


def part_three(s: str):
    bone_scores = [
        {"id": id, "levels": levels, "quality": quality}
        for id, levels, quality in map(build_fishbone, s.splitlines())
    ]

    def sort_cmp(b1, b2):
        q1 = b1["quality"]
        q2 = b2["quality"]
        l1 = b1["levels"]
        l2 = b2["levels"]
        i1 = b1["id"]
        i2 = b2["id"]
        if q1 > q2:
            return -1
        elif q1 < q2:
            return 1

        assert q1 == q2
        differing = next(((x, y) for x, y in zip(l1, l2) if x != y), None)

        if differing is None:
            return 1 if i1 > i2 else -1

        d1 = from_digits(differing[0])
        d2 = from_digits(differing[1])
        assert d1 != d2

        return 1 if d1 < d2 else -1

    ordered = sorted(bone_scores, key=cmp_to_key(sort_cmp))
    return sum(x * y for x, y in enumerate([x["id"] for x in ordered], 1))


ex1 = "58:5,3,7,8,9,10,4,5,7,8,8"

ex2 = """1:2,4,1,1,8,2,7,9,8,6
2:7,9,9,3,8,3,8,8,6,8
3:4,7,6,9,1,8,3,7,2,2
4:6,4,2,1,7,4,5,5,5,8
5:2,9,3,8,3,9,5,2,1,4
6:2,4,9,6,7,4,1,7,6,8
7:2,3,7,6,2,2,4,1,4,2
8:5,1,5,6,8,3,1,8,3,9
9:5,7,7,3,7,2,3,8,6,7
10:4,1,9,3,8,5,4,3,5,5"""

ex3 = """1:7,1,9,1,6,9,8,3,7,2
2:6,1,9,2,9,8,8,4,3,1
3:7,1,9,1,6,9,8,3,8,3
4:6,1,9,2,8,8,8,4,3,1
5:7,1,9,1,6,9,8,3,7,3
6:6,1,9,2,8,8,8,4,3,5
7:3,7,2,2,7,4,4,6,3,1
8:3,7,2,2,7,4,4,6,3,7
9:3,7,2,2,7,4,1,6,3,7"""

ex4 = """7:3,7,2,2,7,4,4,6,3,1
8:3,7,2,2,7,4,4,6,3,7
"""

ex5 = """2:7,1,9,1,6,9,8,3,7,2
1:7,1,9,1,6,9,8,3,7,2"""

ex6 = """1:5,3,7,8,1,10,9,5,7,8
2:5,3,7,8,1,10,9,4,7,9"""

ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(ex3))
ic(part_three(get_notes(3)))
