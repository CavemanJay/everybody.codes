from enum import IntFlag
from functools import reduce
from itertools import accumulate, count, cycle, groupby, islice, permutations
import itertools
from math import factorial
import math
from pprint import pprint
from typing import Callable
from icecream import ic
from everybodycodes.utils import get_notes, loop, print_aligned, transpose


def part_one(s: str):
    stamps = [1, 3, 5, 10][::-1]
    brightnesses = list(int(b) for b in s.splitlines())
    beetles: list[list[int]] = []
    for brightness in brightnesses:
        beetle_stamps = []
        while brightness != 0:
            biggest = next(stamp for stamp in stamps if stamp <= brightness)
            brightness -= biggest
            beetle_stamps.append(biggest)
        beetles.append(beetle_stamps)
    return sum(len(stamps) for stamps in beetles)


ex = """2
4
7
16"""

# ic(part_one(ex))
ic(part_one(get_notes(1)))
