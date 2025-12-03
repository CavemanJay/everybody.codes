import itertools
from pprint import pprint
import re

from icecream import ic

from ..utils import get_notes


def part_one(s: str):
    nail_lengths  = [int(x)for x in s.splitlines()]
    smallest=min(nail_lengths)
    return sum(x-smallest for x in nail_lengths)


ex = """3
4
7
8"""

ic(part_one(get_notes(1)))
ic(part_one(get_notes(2)))
