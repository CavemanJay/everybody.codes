from icecream import ic
from itertools import permutations, combinations

from everybodycodes.utils import get_notes


def part_one(s: str):
    return sum(set(int(d) for d in s.split(",")))


def part_two(s: str):
    nums = (int(d) for d in s.split(","))
    ordered = sorted(set(nums), reverse=True)
    # TODO: This is too slow
    return min(sum(combo) for combo in combinations(ordered, 20))


ex1 = "10,5,1,10,3,8,5,2,2"
ex2 = "4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77"

ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
