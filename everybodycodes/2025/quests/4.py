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


def part_three(s: str):
    nums = [int(x) for gear_pair in s.splitlines() for x in gear_pair.split("|")]
    pairs = list(pairwise(nums))[::2]
    return int(reduce(lambda x, y: x * y, (x / y for x, y in pairs)) * 100)


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

ex3 = """10
7|14
8|16
6"""

ex4 = """5
5|10
10|20
5"""

ex5 = """5
7|21
18|36
27|27
10|50
10|50
11"""


ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))
