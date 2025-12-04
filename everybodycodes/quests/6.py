import itertools
from pprint import pprint
import re
from icecream import ic
from ..utils import get_notes


def parse_line(line: str):
    root, nodes = line.split(":")
    nodes = nodes.split(",")
    return root, nodes


def find_next(lines: list[str], chains: list[list[str]]):
    if chains == []:
        next_line = next(line for line in lines if line.startswith("RR:"))
        lines.remove(next_line)
        return [next_line]

    trailing = list(chain[-1] for chain in chains)
    next_lines = list(
        line for node in trailing for line in lines if line.startswith(node + ":")
    )
    for l in next_lines:
        lines.remove(l)
    return next_lines


def build_chains(s: str):
    lines = s.splitlines()
    chains: list[list[str]] = []
    while lines != []:
        next_lines = find_next(lines, chains)
        if chains == []:
            root, nodes = parse_line(next_lines[0])
            chains.extend([root, node] for node in nodes)
            continue

        for line in next_lines:
            root, nodes = parse_line(line)
            matching_chains = list(c for c in chains if c[-1] == root)
            for chain in matching_chains:
                chains.remove(chain)
                chains.extend(chain + [node] for node in nodes)
    return chains


def fruit_chains(s: str):
    return (c for c in build_chains(s) if c[-1] == "@")


def unique_fruit_chain(s: str):
    chains = fruit_chains(s)
    chains_by_length = itertools.groupby(chains, lambda c: len(c))
    return next(
        group[0]
        for group in (list(group) for chain_length, group in chains_by_length)
        if len(group) == 1
    )


def part_one(s: str):
    return "".join(unique_fruit_chain(s))


def part_two(s: str):
    return "".join(node[0] for node in unique_fruit_chain(s))


ex = """
RR:A,B,C
A:D,E
B:F,@
C:G,H
D:@
E:@
F:@
G:@
H:@
"""[
    1:-1
]

# ic(part_one(ex))
ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
