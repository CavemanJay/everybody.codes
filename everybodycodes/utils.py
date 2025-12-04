import inspect
from itertools import cycle, islice, zip_longest
import pathlib
from typing import Iterable, Sequence


def get_notes(part: int):
    x = pathlib.Path(f"everybodycodes/notes/{get_current_quest()}_{part}.txt")
    with open(x.absolute().resolve().as_posix()) as f:
        return f.read()


def throw(msg=""):
    raise Exception(msg)


def get_current_quest(n=2):
    caller_frame = inspect.stack()[n]
    caller_module = inspect.getmodule(caller_frame[0]) or throw(
        "Couldn't get module name",
    )
    return int(caller_module.__name__.split(".")[-1])


def transpose_jagged[T](
    grid: Sequence[Sequence[T | None]],
) -> Sequence[Sequence[T | None]]:
    return list(list(x) for x in zip_longest(*grid, fillvalue=None))


def transpose[T](grid: Sequence[Sequence[T]]) -> list[list[T]]:
    return list(list(x) for x in zip(*grid))


def loop[T](i: Iterable[T], n: int):
    return islice(cycle(i), n)
