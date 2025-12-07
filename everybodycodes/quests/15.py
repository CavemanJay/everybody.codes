from collections import deque
from itertools import groupby, product
from typing import Iterable

from icecream import ic

from everybodycodes.utils import get_notes, sliding_window


Coord = tuple[int, int]
Target = tuple[Coord, str]


def shortest_path_2d(start: Coord, goal: Coord, valid_coords: Iterable[Coord]) -> int:
    valid = set(valid_coords)
    if start not in valid or goal not in valid:
        raise Exception("WHAT?")

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist

        # 4 possible neighbor moves
        for nx, ny in [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]:
            neighbor = (nx, ny)
            if neighbor in valid and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    raise Exception("There should always be a path")


def parse(s: str):
    grid = list(list(line) for line in s.splitlines())
    start_col = next(c for c, char in enumerate(grid[0]) if char == ".")

    queue = deque([((0, start_col), 0)])
    visited: set[Coord] = set([(0, start_col)])
    targets: set[Target] = set()

    while queue:
        (r, c), dist = queue.popleft()
        for nr, nc in (
            coord
            for coord in (
                (r + 1, c) if r < len(grid) - 1 else None,
                (r - 1, c) if r > 0 else None,
                (r, c + 1) if c < len(grid[r]) else None,
                (r, c - 1) if c > 0 else None,
            )
            if coord is not None
        ):
            neighbor = (nr, nc)
            val = grid[nr][nc]
            if val not in "#~" and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                if val != ".":
                    targets.add((neighbor, val))
    return (0, start_col), visited, targets


def part_one(s: str):
    start, valid, targets = parse(s)
    return min(shortest_path_2d(start, t[0], valid) * 2 for t in targets)


def part_two(s: str):
    start, valid, targets = parse(s)
    targets_by_type = groupby(sorted(targets, key=lambda t: t[1]), key=lambda t: t[1])
    groups = list((key, list(val)) for key, val in targets_by_type)

    # Generate all permutations: 1 element from each group
    lists = [vals for _, vals in groups]
    combos = list(product(*lists))

    shortest = float("inf")
    for combo in combos:
        # combo = ((start, "S"),) + combo + ((start, "E"),)
        combo = (
            ((start, "S"),)
            + (((3, 3), "A"), ((7, 1), "C"), ((6, 8), "B"))
            + ((start, "E"),)
        )
        w = sliding_window(combo, 2)
        distances = list(shortest_path_2d(s[0], e[0], valid) for s, e in w)
        shortest = min(shortest, sum(distances) - 2)
    return shortest


ex1 = """#####.#####
#.........#
#.######.##
#.........#
###.#.#####
#H.......H#
###########"""

ex2 = """##########.##########
#...................#
#.###.##.###.##.#.#.#
#..A#.#..~~~....#A#.#
#.#...#.~~~~~...#.#.#
#.#.#.#.~~~~~.#.#.#.#
#...#.#.B~~~B.#.#...#
#...#....BBB..#....##
#C............#....C#
#####################"""

# ic(part_one(get_notes(1)))
ic(part_two(ex2))
# ic(part_two(get_notes(2)))
