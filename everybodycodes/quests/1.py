import itertools as itertools
from typing import Sequence

from icecream import ic

from ..utils import get_notes

potion_map = {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}


def part_one(s: Sequence[str]):
	# return functools.reduce(lambda x, y: x + potion_map[y], s, 0)
	return sum(potion_map[m] for m in s)


def part_two(s: Sequence[str]):
	def tally(duo: Sequence[str]):
		return part_one(duo) + (0 if 'x' in duo else 2)

	return sum(tally(duo) for duo in itertools.batched(s, 2))


def part_three(s: str):
	def tally(trio: Sequence[str]):
		match sum(1 for x in trio if x != 'x'):
			case 0:
				return 0
			case 1:
				return part_one(trio)
			case 2:
				return part_two(trio)
			case 3:
				return part_one(trio) + 2 * len(trio)
		return sum(potion_map[m] for m in trio)

	return sum(tally(trio) for trio in itertools.batched(s, 3))


ic(part_one(get_notes(1)))
ic(part_two(get_notes(1, 2)))
ic(part_three(get_notes(1, 3)))

