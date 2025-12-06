import plotly.graph_objects as go
from enum import IntFlag
from functools import reduce
from itertools import accumulate, count, cycle, groupby, islice, pairwise, permutations
import itertools
from math import factorial
import math
import os
from pprint import pprint
from typing import Callable, Iterable, Sequence
from icecream import ic
from ..utils import get_notes, loop, print_aligned, transpose

# (dx,dy,dz)
instructions = {
    "U": (0, 1, 0),
    "D": (0, -1, 0),
    "R": (1, 0, 0),
    "L": (-1, 0, 0),
    "F": (0, 0, 1),
    "B": (0, 0, -1),
}


def get_steps(s: str):
    for delta in (
        tuple(int(x[1:]) * ins for ins in instructions[x[0]]) for x in s.split(",")
    ):
        assert len(delta) == 3
        yield delta


# def format_plant(segments: Iterable[tuple[int, int]]):
#     min_x = min(x for x, y in segments)
#     max_x = max(x for x, y in segments)
#     min_y = min(y for x, y in segments)
#     max_y = max(y for x, y in segments)
#     out = ""
#     for y in range(min_y, max_y + 1):
#         line = ""
#         for x in range(min_x - 1, max_x + 2):
#             line += "#" if (x, y) in segments else "."
#         out += line[::-1]
#         out += "\n"
#     return (out[::-1] + "\n" + "=" * (max_x - min_x + 3)).strip()


def render_plant(segments: Iterable[tuple[int, int, int]]):
    segments = [(x, y, -z) for x, y, z in segments]
    xs, ys, zs = zip(*segments)
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=xs, y=ys, z=zs, mode="markers", marker=dict(size=6, color="blue")
            )
        ]
    )

    fig.update_layout(
        # scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        scene=dict(
            xaxis=dict(title="X", dtick=1),
            yaxis=dict(title="Y", dtick=1),
            zaxis=dict(title="Z", dtick=1),
            aspectmode="cube",
        ),
        # scene_camera=dict(
        #     eye=dict(x=-1.5, y=1.5, z=1.8),  # choose viewpoint
        #     up=dict(x=0, y=0, z=1),  # z-axis is upward
        # ),
        scene_camera=dict(
            # eye=dict(x=0, y=1, z=0),
            up=dict(x=0, y=1, z=0),
        ),
        title="3D Point Cloud Viewer",
    )

    fig.write_html("plant.html", auto_open=False)


def part_one(s: str):
    height = 0
    m = 0
    for height_change in (y for _, y, _ in get_steps(s)):
        height += height_change
        m = max(height, m)
    return m


def part_two(s: str):
    combined_segments = set()
    for line in s.splitlines():
        steps = get_steps(line)
        x, y, z = (0, 0, 0)
        line_segments = set()
        for dx, dy, dz in steps:
            segments = [
                (
                    x + (i + 1 if dx != 0 else 0) * (-1 if dx < 0 else 1),
                    y + (i + 1 if dy != 0 else 0) * (-1 if dy < 0 else 1),
                    z + (i + 1 if dz != 0 else 0) * (-1 if dz < 0 else 1),
                )
                for i in range(max(abs(dx), abs(dy), abs(dz)))
            ]
            line_segments.update(segments)
            x += dx
            y += dy
            z += dz
            # render_plant(line_segments)
            pass
        # render_plant(line_segments)
        combined_segments.update(line_segments)

    render_plant(combined_segments)
    return len(combined_segments)


ex1 = """U5,R3,D2,L5,U4,R5,D2"""

ex2 = """
U5,R3,D2,L5,U4,R5,D2
U6,L1,D2,R3,U2,L1"""[
    1:
]

ex3 = """
U5,F1,R3,F1,D2,F1,L5,F1,U4,F1,R5,F1,D2
U6,L1,D2,R3,U2,L1"""[
    1:
]


# ic(part_one(ex1))
# ic(part_two(ex2))
# ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
