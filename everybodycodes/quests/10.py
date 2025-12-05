from collections import Counter
from enum import IntFlag
from functools import reduce
from itertools import (
    accumulate,
    chain,
    count,
    cycle,
    groupby,
    islice,
    pairwise,
    permutations,
)
import itertools
from math import factorial
import math
from pprint import pprint
from typing import Callable
from icecream import ic
from ..utils import get_notes, loop, print_aligned, transpose


def word_power(word: str):
    return sum((i * (ord(c) - ord("A") + 1)) for i, c in enumerate(word, 1))


def solve_apparent(grid: list[list[str]]):
    assert len(grid) == 8
    assert len(grid[0]) == 8
    modified = False
    for r in range(2, 2 + 4):
        row = grid[r]
        for c in range(2, 2 + 4):
            if row[c] != ".":
                continue
            for col_char in (row[c] for row in grid if row[c] != "."):
                if col_char in row:
                    row[c] = col_char
                    modified = True
                    break
    return modified


def get_word(grid: list[list[str]]):
    assert len(grid) == 8
    assert len(grid[0]) == 8
    word = "".join(chain(*(grid[dr][2:6] for dr in range(2, 6))))

    return word


def solve_hidden(grid: list[list[str]]):
    modified = False
    for r in range(len(grid)):
        row = grid[r]
        for c in range(len(grid[0])):
            if row[c] != ".":
                continue
            col_chars = list(row[c] for r_, row in enumerate(grid) if r_ != r)
            if "." in col_chars:
                continue
            missing_row_char_count = sum(1 for char in row if char in ["?", "."])
            if missing_row_char_count > 2:
                continue
            row_chars = list(char for char in row if char not in ["?", "."])
            missing_chars = list(
                char
                for char, count in Counter(col_chars + row_chars).items()
                if count == 1 and char != '?'
            )
            assert len(missing_chars) == 1
            holes = set(
                chain(
                    ((r, i) for i, char in enumerate(row) if char in ["?", "."]),
                    ((r_, c) for r_, row in enumerate(grid) if row[c] in ["?", "."]),
                )
            )
            assert len(holes) == 2
            for hr, hc in holes:
                grid[hr][hc] = missing_chars[0]
                modified = True
    return modified


def decode(grid: list[list[str]]):
    modified = True
    while modified:
        modified = solve_apparent(grid)
        flatten_grid = lambda: [c for line in grid for c in line]
        if (not "." in flatten_grid()) and (not "?" in flatten_grid()):
            return grid

        modified = modified | solve_hidden(grid)

    return grid


def merge_grids[T](grid: list[list[T]], sub_grid: list[list[T]], i: int, j: int):
    for r in range(len(sub_grid)):
        for c in range(len(sub_grid[0])):
            grid[i + r][j + c] = sub_grid[r][c]


def format_wall(grid: list[list[str]]):
    s = ""
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            s += char
            # if c % 6 == 0:
            #     s += " "
        # if r % 6 == 0:
        #     s += "\n"
        s += "\n"
    return s.strip()


def format_blocks(block_grid: list[list[list[list[str]]]]):
    s = ""
    for grid_row in block_grid:
        y = "\n".join(
            "".join(chain(*[y + [" "] for y in z])).strip()
            for z in zip(*(x for x in grid_row))
        )
        s += y + "\n\n"
    return s.strip()


def part_one(s: str):
    return get_word(decode(list(list(line) for line in s.splitlines())))


def part_two(s: str):
    grids: list[list[list[str]]] = []
    for row in s.split("\n\n"):
        row_lines = row.splitlines()
        splits = [(x, x + 8) for x in range(0, len(row) // 8, 9)]
        for start, stop in splits:
            grid = [row_lines[i][start:stop] for i in range(len(row_lines))]
            grids.append(list(list(line) for line in grid))
    return sum(word_power(get_word(decode(grid))) for grid in grids)


def part_three(s: str):
    grid = list(list(line) for line in s.splitlines())
    words = []
    blocks: list[list[list[list[str]]]] = []
    for i in range(0, len(grid) - 5, 6):
        grid_row = []
        for j in range(0, len(grid[0]) - 5, 6):
            sub_grid = [row[j : j + 8] for row in grid[i : i + 8]]
            try:
                decode(sub_grid)
            except:
                pass
            merge_grids(grid, sub_grid, i, j)
            grid_row.append(sub_grid)
            word = get_word(sub_grid)
            if "." not in word:
                words.append(word)
        blocks.append(grid_row)
    open("wall.txt", "w").write(format_wall(grid))
    open("blocks.txt", "w").write(format_blocks(blocks))
    return sum(map(word_power, words))


ex1 = """**PCBS**
**RLNW**
BV....PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**"""

ex3 = """**XFZB**DCST**
**LWQK**GQJH**
?G....WL....DQ
BS....H?....CN
P?....KJ....TV
NM....Z?....SG
**NSHM**VKWZ**
**PJGV**XFNL**
WQ....?L....YS
FX....DJ....HV
?Y....WM....?J
TJ....YK....LP
**XRTK**BMSP**
**DWZN**GCJV**"""

ex4 = """**XFZB**
**LWQK**
?G....WL
BS....H?
P?....KJ
NM....Z?
**NSHM**
**PJGV**"""

ex5 = """**XFZB**DCST**
**LWQK**GQJH**
?G....WL....DQ
BS....H?....CN
P?....KJ....TV
NM....Z?....SG
**NSHM**VKWZ**
**PJGV**XFNL**"""

ex6 = """**B?DJ**
**?V??**
DH....MS
WT....VQ
XG....RB
JF....ZL
**LFTW**
**HGXS**"""


ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))

# print(format_wall(decode(list(list(line) for line in ex6.splitlines()))))

# ic(part_three(ex3))
# pprint(decode(list(list(line) for line in ex4.splitlines()))[1])
# pprint(decode(list(list(line) for line in ex5.splitlines()))[1])
