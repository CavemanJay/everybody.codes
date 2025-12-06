from itertools import count
from pwn import *
import subprocess

context.log_level = "debug"

for _ in count():
    l = listen(1337, "127.0.0.1").wait_for_connection()
    pid = l.recvline().strip()
    pid = unpack(pid)
    l.sendline()
    subprocess.run(["py-spy", "record", "--pid", str(pid), "-o", f"flamegraph.svg"])
