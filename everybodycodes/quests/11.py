from collections import Counter
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


def gens(rules: str, start_gen: list[str]):
    lookup = {
        k: v.split(",") for k, v in (line.split(":") for line in rules.splitlines())
    }
    prev = Counter(start_gen)
    for _ in itertools.count():
        current: Counter[str] = Counter()
        for key, count in prev.items():
            assert isinstance(key, str)
            new = lookup[key] * count
            current.update(new)
        prev = current
        yield current


def part_one(s: str):
    gen = 4
    return sum(next(islice(gens(s, ["A"]), gen - 1, gen)).values())


def part_two(s: str):
    gen = 10
    return sum(next(islice(gens(s, ["Z"]), gen - 1, gen)).values())


ex1 = """A:B,C
B:C,A
C:A"""

# ic(part_one(ex1))
ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
