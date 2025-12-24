from icecream import ic
from everybodycodes.utils import get_notes

OptInt = int | None


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

    return id, levels, spine


def part_one(s: str):
    _, _, spine = build_fishbone(s)
    return "".join(str(d) for d in spine)


def part_two(s: str):
    bone_scores = [
        int("".join(str(d) for d in spine))
        for _, _, spine in map(build_fishbone, s.splitlines())
    ]
    return max(bone_scores) - min(bone_scores)


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

ic(part_one(ex1))
ic(part_one(get_notes(1)))
ic(part_two(ex2))
ic(part_two(get_notes(2)))
