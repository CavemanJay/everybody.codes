from collections import deque
from icecream import ic

Coord = tuple[int, int]


def part_one(s: str):
    grid = list(list(line) for line in s.splitlines())
    positions = list(
        ((r, c), char) for r, row in enumerate(grid) for c, char in enumerate(row)
    )
    start = next(
        (r, c)
        for ((r, c), char) in positions
        if char == "."
        and (r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1)
    )

    queue = deque([start])
    visited: set[Coord] = set([start])
    targets: set[Coord] = set(pos for (pos, char) in positions if char == "P")

    i = 0
    found = 0
    while queue:
        (r, c) = queue.popleft()
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
            if val not in "#" and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                found += 1

        if found == len(targets):
            return i
        i += 1

    return i


ex1 = """##########
..#......#
#.P.####P#
#.#...P#.#
##########"""

ic(part_one(ex1))
