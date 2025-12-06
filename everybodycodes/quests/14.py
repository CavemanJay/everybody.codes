from collections import Counter, deque
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
    "F": (0, 0, -1),
    "B": (0, 0, 1),
}

Coord = tuple[int, int, int]


def get_steps(s: str):
    for delta in (
        tuple(int(x[1:]) * ins for ins in instructions[x[0]]) for x in s.split(",")
    ):
        assert len(delta) == 3
        yield delta


# AI Generated
def shortest_path_3d(start: Coord, goal: Coord, valid_coords: Iterable[Coord]) -> int:
    valid = set(valid_coords)
    if start not in valid or goal not in valid:
        raise Exception("WHAT?")

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y, z), dist = queue.popleft()
        if (x, y, z) == goal:
            return dist

        # 6 possible neighbor moves
        for nx, ny, nz in [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]:
            neighbor = (nx, ny, nz)
            if neighbor in valid and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    raise Exception("There should always be a path")


def render_plant(
    segments: Iterable[Coord],
    *,
    leafs: Iterable[Coord] | None = None,
    trunk: Iterable[Coord] | None = None,
):

    leafs = [] if leafs is None else leafs
    xs_s, ys_s, zs_s = zip(*segments)
    xs_l, ys_l, zs_l = zip(*leafs) if leafs else [[], [], []]
    xs_t, ys_t, zs_t = zip(*trunk) if trunk else [[], [], []]
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=xs_s,
                y=ys_s,
                z=zs_s,
                mode="markers",
                marker=dict(size=6, color="blue"),
                name="Branches",
            ),
            go.Scatter3d(
                x=xs_l,
                y=ys_l,
                z=zs_l,
                mode="markers",
                marker=dict(size=6, color="green"),
                name="Leafs",
            ),
            go.Scatter3d(
                x=xs_t,
                y=ys_t,
                z=zs_t,
                mode="markers",
                marker=dict(size=6, color="brown"),
                name="Trunk",
            ),
        ]
    )

    fig.update_layout(
        # scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        scene=dict(
            xaxis=dict(title="X", dtick=1),
            yaxis=dict(title="Y", dtick=1),
            zaxis=dict(title="Z", dtick=1),
            # aspectmode="cube",
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
                for i in range(max(map(abs, [dx, dy, dz])))
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


def part_three(s: str):
    combined_segments: set[Coord] = set()
    leafs: Counter[Coord] = Counter()
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
                for i in range(max(map(abs, [dx, dy, dz])))
            ]
            line_segments.update(segments)
            x += dx
            y += dy
            z += dz
            # render_plant(line_segments)
            # pass
        leafs.update([(x, y, z)])
        # render_plant(line_segments)
        combined_segments.update(line_segments)

    def gen_trunk():
        it = iter(
            sorted(
                ((x, y, z) for x, y, z in combined_segments if x | z == 0),
                key=lambda x: x[1],
            )
        )
        prev = next(it)
        yield prev
        for curr in it:
            if curr[1] - prev[1] == 1:
                yield curr
                prev = curr
            else:
                break

    trunk = list(gen_trunk())
    unique_leafs = (
        [coords for coords, count in leafs.items() if count == 1] if True else leafs
    )

    render_plant(combined_segments, leafs=leafs, trunk=trunk)

    def distance_to_leafs(t: Coord):
        return sum(
            shortest_path_3d(t, leaf, combined_segments) for leaf in unique_leafs
        )

    return min(distance_to_leafs(t) for t in trunk)


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

ex4 = """U5,R3,D2,L5,U4,R5,D2
U6,L1,D2,R3,U2,L1"""

ex5 = """U20,L1,B1,L2,B1,R2,L1,F1,U1
U10,F1,B1,R1,L1,B1,L1,F1,R2,U1
U30,L2,F1,R1,B1,R1,F2,U1,F1
U25,R1,L2,B1,U1,R2,F1,L2
U16,L1,B1,L1,B3,L1,B1,F1"""


ic(part_one(get_notes(1)))
ic(part_two(get_notes(2)))
ic(part_three(get_notes(3)))
