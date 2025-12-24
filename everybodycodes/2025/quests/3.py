from icecream import ic

from everybodycodes.utils import get_notes


def part_one(s: str):
    return sum(set(int(d) for d in s.split(",")))


ex1 = "10,5,1,10,3,8,5,2,2"

ic(part_one(get_notes(1)))
