#!/usr/bin/env python
"""Run in Python the command with timeout:

  $ while ! python example.py 2>&1|tee out|grep '^$';do echo -n .;done;cat out'
"""
import os, signal, sys
import time
from subprocess import Popen
from timeit import default_timer as timer 

timeout = 30
cmd = """while ! %(python)s example.py 2>&1|tee out |grep '^$'
do echo -n .
done
cat out
""" % dict(python=sys.executable)
p = Popen(cmd, shell=True)

# kill the process on timeout
start = timer()
while p.poll() is None:
    if (timer() -  start) > timeout:
        os.kill(p.pid, signal.SIGKILL) # compatibility with 2.4
        os.waitpid(-1, os.WNOHANG)
        sys.exit(0) # It might be OK
    time.sleep(.1)
assert p.returncode, "empty line encountered"
