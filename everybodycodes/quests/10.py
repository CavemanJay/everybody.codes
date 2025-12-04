from enum import IntFlag
from functools import reduce
from itertools import accumulate, count, cycle, groupby, islice, permutations
import itertools
from math import factorial
import math
from pprint import pprint
from typing import Callable
from icecream import ic
from ..utils import get_notes, loop, print_aligned, transpose


def part_one(s: str):
    grid = list(list(l) for l in s.splitlines())
    word = ""
    for r in range(2, 2 + 4):
        row = grid[r]
        for c in range(2, 2 + 4):
            for col_char in (row[c] for row in grid if row[c] != "."):
                if col_char in row:
                    row[c] = col_char
                    word += col_char
                    break
    return word


ex1 = """**PCBS**
**RLNW**
BV....PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**"""

# ic(part_one(ex1))
ic(part_one(get_notes(1)))
