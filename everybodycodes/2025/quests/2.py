from icecream import ic
from typing import TypeAlias
import ast
import plotly.graph_objects as go
from concurrent.futures import ProcessPoolExecutor


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
            (self.x * other.x) - (self.y * other.y),
            (self.x * other.y) + (self.y * other.x),
        )

    def __truediv__(self, other: "ComplexNum | ImplicitComplex"):
        if isinstance(other, tuple):
            other = ComplexNum(other[0], other[1])
        return ComplexNum(int(self.x / other.x), int(self.y / other.y))

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"


def render(engraved: list[ComplexNum]):
    x = [p.x for p in engraved]
    y = [p.y * -1 for p in engraved]
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode="markers"))
    fig.update_layout(title="Coordinate Plot", xaxis_title="X", yaxis_title="Y")
    fig.update_layout(
        xaxis=dict(range=[min(x) - 10, max(x) + 10]),
        yaxis=dict(range=[min(y) - 10, max(y) + 10]),
    )
    fig.show()


def parse_a(s: str):
    return ComplexNum(*tuple(ast.literal_eval(s.split("=", 1)[-1])))


def part_one(s: str):
    r = ComplexNum(0, 0)
    A = parse_a(s)
    for _ in range(3):
        r *= r
        r /= (10, 10)
        r += A

    return r


def part_two(s: str):
    A = parse_a(s)
    opp_corner = A + (1000, 1000)
    limit = 1000000
    engraved: list[ComplexNum] = []
    for x in range(A.x, opp_corner.x + 1, 10):
        for y in range(A.y, opp_corner.y + 1, 10):
            r = ComplexNum(0, 0)
            for i in range(100):
                r *= r
                try:
                    r /= (100000, 100000)
                except:
                    break
                r += (x, y)
                if abs(r.x) > limit or abs(r.y) > limit:
                    break
            else:
                engraved.append(ComplexNum(x, y))

    return len(engraved)


def _check_line(x: int, y_range: range):
    engraved: list[ComplexNum] = []
    limit = 1000000
    for y in y_range:
        r = ComplexNum(0, 0)
        for i in range(100):
            r *= r
            try:
                r /= (100000, 100000)
            except:
                break
            r += (x, y)
            if abs(r.x) > limit or abs(r.y) > limit:
                break
        else:
            engraved.append(ComplexNum(x, y))
    return engraved


def part_three(s: str):
    A = parse_a(s)
    grid_size = 1001
    steps = grid_size - 1
    corner_distance = 1000
    step_size = corner_distance // steps
    opp_corner = A + (corner_distance, corner_distance)

    x_range = range(A.x, opp_corner.x + 1, step_size)
    y_range = range(A.y, opp_corner.y + 1, step_size)

    with ProcessPoolExecutor() as ex:
        results = ex.map(_check_line, x_range, [y_range] * len(x_range))
    engraved = [p for line in results for p in line]

    # render(engraved)
    return len(engraved)


ex1 = "A=[25,9]"
ex2 = "A=[35300,-64910]"


# ic(part_one(get_notes(1)))
# ic(part_two(get_notes(2)))
ic(part_three(ex2))
