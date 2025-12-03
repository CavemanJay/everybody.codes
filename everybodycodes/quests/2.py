import itertools as itertools
import re

from icecream import ic

from ..utils import get_notes

def parse_input(s: str):
	pattern = r'words:(?P<runes>\S+)\n\n(?P<script>.*)'
	m = re.search(pattern, s, re.I | re.M)
	if m is None:
		raise Exception()
	return (m.group('runes').split(','), m.group('script'))


def part_one(s: str):
	runes, inscription = parse_input(s)
	# return "POWE PO WER P OWE R".count("OWE")
	return sum(inscription.count(rune) for rune in runes)


x = """
WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE
"""

ic(part_one(get_notes(1)))
