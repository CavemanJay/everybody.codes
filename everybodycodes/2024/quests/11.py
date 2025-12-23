from collections import defaultdict
from itertools import islice
import itertools
from icecream import ic
from everybodycodes.utils import get_notes


def gens(rules: str, start_gen: list[str]):
    lookup = {
        k: v.split(",") for k, v in (line.split(":") for line in rules.splitlines())
    }
    prev = defaultdict(int)
    for termite in start_gen:
        prev[termite] += 1

    for _ in itertools.count():
        current = defaultdict(int)
        for key, count in prev.items():
            for termite in lookup[key]:
                current[termite] += count
        prev = current
        yield current


def population_size(s: str, gen: int, start_gen: "list[str]"):
    return sum(next(islice(gens(s, start_gen), gen - 1, gen)).values())


def part_one(s: str):
    return population_size(s, 4, ["A"])


def part_two(s: str):
    return population_size(s, 10, ["Z"])


def part_three(s: str):
    gen = 20
    pop_sizes = [
        population_size(s, gen, start_gen)
        for start_gen in ([line.split(":")[0]] for line in s.splitlines())
    ]
    return max(pop_sizes) - min(pop_sizes)


ex1 = """A:B,C
B:C,A
C:A"""

ex2 = """A:B,C
B:C,A,A
C:A"""

# ic(part_one(ex1))
ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))
