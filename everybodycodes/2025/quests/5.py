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




ex1 = "58:5,3,7,8,9,10,4,5,7,8,8"

ic(part_one(ex1))
ic(part_one(get_notes(1)))
