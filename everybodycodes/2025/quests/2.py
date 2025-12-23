from icecream import ic
from typing import TypeAlias
import ast

from everybodycodes.utils import get_notes

ImplicitComplex: TypeAlias = tuple[int, int]


class ComplexNum:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "ComplexNum | ImplicitComplex"):
        if isinstance(other, tuple):
            other = ComplexNum(other[0], other[1])
        return ComplexNum(self.x + other.x, self.y + other.y)

    def __mul__(self, other: "ComplexNum | ImplicitComplex"):
        if isinstance(other, tuple):
            other = ComplexNum(other[0], other[1])

        return ComplexNum(
            self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x
        )

    def __truediv__(self, other: "ComplexNum | ImplicitComplex"):
        if isinstance(other, tuple):
            other = ComplexNum(other[0], other[1])
        return ComplexNum(self.x // other.x, self.y // other.y)

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"


def part_one(s: str):
    r = ComplexNum(0, 0)
    A = tuple(ast.literal_eval(s.split("=", 1)[-1]))
    for i in range(3):
        r *= r
        r /= (10, 10)
        r += A

    return r


ex1 = "A=[25,9]"


ic(part_one(get_notes(1)))
