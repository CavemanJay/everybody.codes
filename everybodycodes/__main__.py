import importlib
import signal
import subprocess
import sys
import os
import time
from pwn import *

context.log_level = "debug"

def main():
    importlib.import_module(f"everybodycodes.quests.{sys.argv[1]}")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[2] == "record":
        pid = os.getpid()
        print(pid)
        r = remote("localhost", 1337)
        r.sendline(p32(pid))
        r.recvline()

    main()
