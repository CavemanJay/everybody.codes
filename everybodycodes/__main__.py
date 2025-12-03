import importlib
import sys

if __name__ == "__main__":
    module = importlib.import_module(f"everybodycodes.quests.{sys.argv[1]}")
