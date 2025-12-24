from icecream import ic
from itertools import pairwise
from functools import reduce
from math import ceil

from everybodycodes.utils import get_notes

# full_turns_last_gear = pairwise_ratio_product * first_gear_turns
# first_gear_turns = full_turns_last_gear / pairwise_ratio_product


def pairwise_ratio_product(gears: list[int]):
    pairs = pairwise(gears)
    return reduce(lambda x, y: x * y, (x / y for x, y in pairs), 1)


def part_one(s: str):
    nums = [int(x) for x in s.splitlines()]
    return int(pairwise_ratio_product(nums) * 2025)


def part_two(s: str):
    full_turns = 10000000000000
    nums = [int(x) for x in s.splitlines()]
    return ceil(full_turns / pairwise_ratio_product(nums))


ex1 = """128
64
32
16
8"""

ex2 = """102
75
50
35
13"""


ic(part_one(get_notes(1)))
ic(part_two(ex1))
ic(part_two(ex2))
ic(part_two(get_notes(2)))
