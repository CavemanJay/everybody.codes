import importlib
import signal
import subprocess
import sys
import os
import time
from pwn import *

context.log_level = "debug"

def main():
    year = sys.argv[1]
    quest = sys.argv[2]
    importlib.import_module(f"everybodycodes.{year}.quests.{quest}")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[3] == "record":
        pid = os.getpid()
        print(pid)
        r = remote("localhost", 1337)
        r.sendline(p32(pid))
        r.recvline()

    main()
