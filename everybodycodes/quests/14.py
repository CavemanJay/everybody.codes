from enum import IntFlag
from functools import reduce
from itertools import accumulate, count, cycle, groupby, islice, pairwise, permutations
import itertools
from math import factorial
import math
from pprint import pprint
from typing import Callable
from icecream import ic
from ..utils import get_notes, loop, print_aligned, transpose

# (dx,dy,dz)
instructions = {
    "U": (0, 1, 0),
    "D": (0, -1, 0),
    "R": (1, 0, 0),
    "L": (-1, 0, 0),
    "F": (0, 0, 1),
    "B": (0, 0, -1),
}


def get_steps(s: str):
    return list(tuple(int(x[1:]) * ins for ins in instructions[x[0]]) for x in s.split(","))


def part_one(s: str):
    height = 0
    m = 0
    for height_change in  ( y for x,y,z in  get_steps(s)):
        height += height_change
        m = max(height,m)

    return m


ex1 = """U5,R3,D2,L5,U4,R5,D2"""

# ic(part_one(ex1))
ic(part_one(get_notes(1)))
