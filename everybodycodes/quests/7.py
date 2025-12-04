import itertools
import functools
from pprint import pprint
import re
from typing import Callable
from icecream import ic
from ..utils import get_notes


def parse_line(s: str):
    name, ops = s.split(":")
    ops = ops.split(",")
    ops = list(itertools.islice(itertools.cycle(ops), 10))
    return name, ops


def part_one(s: str):
    op_funcs: dict[str, Callable[[int], int]] = {
        "+": lambda x: x + 1,
        "=": lambda x: x,
        "-": lambda x: x - 1,
    }
    devices = map(parse_line, s.splitlines())
    rankings = (
        (
            device,
            sum(
                itertools.accumulate(
                    ops,
                    lambda acc, op: op_funcs[op](acc),
                    # initial=op_funcs[device[1][0]](10),
                    initial=10,
                )
            )
            - 10,
        )
        for device, ops in devices
    )
    return "".join(x[0] for x in sorted(rankings, key=lambda x: x[1], reverse=True))


ex = """A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+"""

# ic(part_one(ex))
ic(part_one(get_notes(1)))
