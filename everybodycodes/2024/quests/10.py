from enum import IntFlag
from functools import reduce
from itertools import accumulate, count, cycle, groupby, islice, pairwise, permutations
import itertools
from math import factorial
import math
from pprint import pprint
from typing import Callable
from icecream import ic
from everybodycodes.utils import get_notes, loop, print_aligned, transpose


def word_power(word: str):
    return sum((i * (ord(c) - ord("A") + 1)) for i, c in enumerate(word, 1))


def decode(sample: str):
    grid = list(list(l) for l in sample.splitlines())
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


def part_one(s: str):
    return decode(s)


def part_two(s: str):
    grids = []
    for row in s.split("\n\n"):
        row_lines = row.splitlines()
        splits = [(x, x + 8) for x in range(0, len(row) // 8, 9)]
        for start, stop in splits:
            grid = [row_lines[i][start:stop] for i in range(len(row_lines))]
            grids.append("\n".join(grid))
    return sum(word_power(decode(grid)) for grid in grids)


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
ic(part_two(get_notes(2)))
