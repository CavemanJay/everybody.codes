from enum import IntFlag
from functools import lru_cache, reduce
from itertools import accumulate, count, cycle, groupby, islice, permutations
import itertools
from math import factorial
import math
from pprint import pprint
from typing import Callable
from icecream import ic
from ..utils import get_notes, loop, print_aligned, transpose


def beetle_stamps(s: str, stamps: list[int]):
    stamps = sorted(stamps)

    @lru_cache
    def min_stamps(bright: int):
        if bright < 1:
            return bright

        min_count = float("inf")
        smaller_stamps = (s for s in stamps if s <= bright)
        for stamp in smaller_stamps:
            count = 1 + min_stamps(bright - stamp)
            if count < min_count:
                min_count = count
        return min_count

    brightnesses = (int(b) for b in s.splitlines())

    beetles = list(min_stamps(b) for b in brightnesses)
    return beetles


def part_one(s: str):
    stamps = [1, 3, 5, 10]
    beetles = beetle_stamps(s, stamps)
    return sum(stamp_count for stamp_count in beetles)


def part_two(s: str):
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    beetles = beetle_stamps(s, stamps)
    return sum(stamp_count for stamp_count in beetles)


ex1 = """2
4
7
16"""

ex2 = """33
41
55
99"""


ic(part_one(ex1))
ic(part_one(get_notes(1)))
ic(part_two(ex2))
