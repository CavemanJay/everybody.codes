from collections import deque
from typing import Iterable

from icecream import ic

from everybodycodes.utils import get_notes


Coord = tuple[int, int]


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
    targets: set[Coord] = set()

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
            if val in ".H" and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                if val == "H":
                    targets.add(neighbor)
    return (0, start_col), visited, targets


def part_one(s: str):
    start, valid, targets = parse(s)
    return min(shortest_path_2d(start, t, valid) * 2 for t in targets)


ex1 = """#####.#####
#.........#
#.######.##
#.........#
###.#.#####
#H.......H#
###########"""

ic(part_one(get_notes(1)))
