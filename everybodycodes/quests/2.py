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


def part_three(s: str):
    runes, inscription = parse_input(s)
    lines = list(line for line in inscription.splitlines())
    # runes = ["RODEO"]
    # lines = [lines[-1]]
    coords = set()
    for row, line in enumerate(lines):
        ic(row,len(lines))
        for col, char in enumerate(line):
            for rune in runes:
                # left to right
                to_check = (
                    line[col::] + line[0:col] if col + len(rune) > len(line) else line[col:]
                )
                if to_check.startswith(rune):
                    coords.add( ( row, col, tuple( (row, col_index % len(line)) for col_index in range(col, len(rune) + col)), rune,))

                # right to left
                to_check = ''.join( line[(col - i) % len(line)] for i in range(len(line)))
                if to_check.startswith(rune):
                    coords.add( ( row, col, tuple( (row, col_index % len(line)) for col_index in (col-x for x in range(len(rune)))), rune,))

                # top to bottom
                to_check = "".join (line[col] for line in lines[row:])
                if to_check.startswith(rune):
                    coords.add( ( row, col, tuple((r,col) for r in range(len(rune))), rune,))
                
                # bottom to top
                to_check = "".join (line[col] for line in lines[row::-1])
                if to_check.startswith(rune):
                    coords.add( ( row, col, tuple((r,col) for r in (row-x for x in range(len(rune)))), rune,))
    return len(set(rune_coord for row,col,rune_coords,rune in coords for rune_coord in rune_coords))


# 01234567
# HELWORLT
# ENIGWDXL
# TRODEOAL

x = """
WORDS:THE,OWE,MES,ROD,RODEO

HELWORLT
ENIGWDXL
TRODEOAL
"""

ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))
