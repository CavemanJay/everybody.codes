import itertools
from pprint import pprint
import re

from icecream import ic

from ..utils import get_notes


def parse_map(s: str):
    return [[-1 if c == "." else 1 for c in line] for line in s.splitlines()]


def get_neighbors(r: int, c: int, grid: list[list[int]]):
    if grid[r][c] == -1:
        return []
    top = grid[r - 1][c]
    bottom = grid[r + 1][c]
    left = grid[r][c - 1]
    right = grid[r][c + 1]
    return list(cell for cell in (top, left, bottom, right) if cell != -1)


def print_aligned(matrix):
    # Find the width needed for each column
    col_widths = [
        max(len(str(row[i])) for row in matrix) for i in range(len(matrix[0]))
    ]

    for row in matrix:
        print(" ".join(str(val).rjust(col_widths[i]) for i, val in enumerate(row)))


def part_one(s: str):
    grid = parse_map(s)
    for layer in itertools.count(2):
        next_grid = [row[:] for row in grid]
        mined = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                neighbors = get_neighbors(r, c, grid)
                if len(neighbors) == 0:
                    continue
                if len(neighbors) != 4:
                    continue
                if sum(1 for x in neighbors if x == layer - 1) < 4:
                    continue
                next_grid[r][c] = cell + 1
                mined += 1
        grid = next_grid
        if mined == 0 or mined == 1:
            break
    return sum(cell for row in grid for cell in row if cell != -1)

part_two = part_one

ex = """..........
..###.##..
...####...
..######..
..######..
...####...
.........."""

ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
