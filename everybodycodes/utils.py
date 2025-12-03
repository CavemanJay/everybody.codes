import pathlib


def get_notes(challenge_num: int, part: int = 1):
	x = pathlib.Path(f'everybodycodes/notes/{challenge_num}_{part}.txt')
	with open(x.absolute().resolve().as_posix()) as f:
		return f.read()
