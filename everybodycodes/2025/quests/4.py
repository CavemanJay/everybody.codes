from icecream import ic
from itertools import pairwise
from functools import reduce

from everybodycodes.utils import get_notes


def part_one(s: str):
    nums = [int(x) for x in s.splitlines()]
    pairs = pairwise(nums)
    return int(reduce(lambda x, y: x * y, (x / y for x, y in pairs), 1) * 2025)


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


ic(part_one(ex1))
ic(part_one(ex2))
ic(part_one(get_notes(1)))
