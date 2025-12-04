import itertools
from pprint import pprint
import re
from icecream import ic
from ..utils import get_notes


def part_one(s: str):
    nail_lengths = [int(x) for x in s.splitlines()]
    smallest = min(nail_lengths)
    return sum(x - smallest for x in nail_lengths)


part_two = part_one


def part_three(s: str):
    nail_lengths = [int(x) for x in s.splitlines()]
    return min((sum(abs(x - target) for x in nail_lengths)) for target in nail_lengths)


ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))
