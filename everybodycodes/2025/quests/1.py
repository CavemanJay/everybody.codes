from icecream import ic

from everybodycodes.utils import get_notes


def parse_input(s: str):
    l = s.splitlines()
    names = l[0].split(",")
    instructions = l[-1].split(",")
    return names, instructions


def part_one(s: str):
    names, instructions = parse_input(s)
    curr = 0
    for ins in instructions:
        direction = 1 if ins[0] == "R" else -1
        amount = int(ins[1:])
        curr += direction * amount
        if curr < 0:
            curr = 0
        if curr >= len(names):
            curr = len(names) - 1

    return names[curr]


ex1 = """Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1"""

ic(part_one(get_notes(1)))
