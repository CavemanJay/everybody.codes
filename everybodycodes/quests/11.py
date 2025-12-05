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


def part_one(s: str):
    lookup = {k: v.split(",") for k, v in (line.split(":") for line in s.splitlines())}

    gens = [Counter(["A"])]
    for _ in range(4):
        current = Counter()
        prev = gens[-1]
        for key, count in prev.items():
            assert isinstance(key, str)
            new = lookup[key] * count
            current.update(new)
        gens.append(current)

    return sum(gens[-1].values())


ex1 = """A:B,C
B:C,A
C:A"""

# ic(part_one(ex1))
ic(part_one(get_notes(1)))
