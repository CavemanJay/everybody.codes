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

# Layer: 0 1 2  3
# Count: 1 4 9 16
# Width: 1 3 5  7


def layer_width(layer: int):
    return 2 * layer - 1


def layer_blocks(layer: int):
    return sum(layer_width(i) for i in range(1, layer + 1))


def part_one(s: str):
    n = int(s)

    for layer in count(1):
        width = layer_width(layer)
        blocks = layer_blocks(layer)
        remaining = n - blocks
        if remaining < 0:
            return width * abs(remaining)


# ic(part_one("13"))
ic(part_one(get_notes(1)))
