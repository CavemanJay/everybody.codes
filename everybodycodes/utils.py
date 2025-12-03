import inspect
import pathlib

def get_notes(part: int):
	x = pathlib.Path(f'everybodycodes/notes/{get_current_quest()}_{part}.txt')
	with open(x.absolute().resolve().as_posix()) as f:
		return f.read()


def throw(msg=''):
	raise Exception(msg)


def get_current_quest(n=2):
	caller_frame = inspect.stack()[n]
	caller_module = inspect.getmodule(caller_frame[0]) or throw(
		"Couldn't get module name"
	)
	return int(caller_module.__name__.split('.')[-1])
