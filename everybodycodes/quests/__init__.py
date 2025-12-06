import importlib
import signal
import subprocess
import sys
import os
import time
from pwn import *

context.log_level = "debug"

print(sys.argv)

if len(sys.argv) == 2 and sys.argv[1] == "record":
    pid = os.getpid()
    print(pid)
    r = remote("localhost", 1337)
    r.sendline(p32(pid))
    r.recvline()
