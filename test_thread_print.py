#!/usr/bin/env python
"""Run in Python the command with timeout:

  $ while ! python example.py 2>&1|tee out|grep '^$';do echo -n .;done;cat out'
"""
import sys
import time
from subprocess import Popen
from timeit import default_timer as timer

timeout = 30
me = time.time()
cmd = """while [ ! -f exit.%(me)s ] &&
               ! %(python)s example.py 2>&1|tee out.%(me)s |grep '^$'
do echo -n .
done
cat out.%(me)s && rm out.%(me)s
[ -f exit.%(me)s ] && rm exit.%(me)s && exit 1 || exit 0
""" % dict(python=sys.executable, me=me)
p = Popen(cmd, shell=True)

# kill the process on timeout
start = timer()
while p.poll() is None:
    if (timer() -  start) > timeout:
        # p has no pid on jython so we can't use os.kill()
        # touch exit.*
        open('exit.%s' % (me,), 'wb').close()
        p.wait()
    time.sleep(1)
assert p.returncode, "empty line encountered"
