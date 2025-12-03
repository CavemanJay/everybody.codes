import itertools
import re

from icecream import ic

from ..utils import get_notes


def parse_input(s: str):
    pattern = r"words:(?P<runes>\S+)\n\n(?P<script>.*)"
    m = re.search(pattern, s, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    if m is None:
        raise Exception
    return (m.group("runes").split(","), m.group("script"))


def get_rune_symbol_occurrences(rune: str, inscription: str):
    """Returns a list of (start_index, matching_rune)"""
    return [
        (i, rune) for i in range(len(inscription)) if inscription.startswith(rune, i)
    ]


def part_one(s: str):
    runes, inscription = parse_input(s)
    return sum(
        sum(1 for _ in get_rune_symbol_occurrences(rune, inscription)) for rune in runes
    )


def part_two(s: str):
    runes, inscription = parse_input(s)
    runes = list(set(x for rune in runes for x in [rune, rune[::-1]]))
    # Count the unique indexes that get matched
    return len(
        set(
            matched_indices
            for rune_matches in filter(
                lambda x: x,
                (get_rune_symbol_occurrences(rune, inscription) for rune in runes),
            )
            for index, rune in rune_matches
            for matched_indices in range(index, index + len(rune))
        )
    )


x = """
WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ
"""

ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
