"""Run until empty line is found:

   $ while ! python example.py 2>&1|tee out|grep '^$';do echo -n .;done;cat out
"""
from __future__ import print_function
import random, sys, time
import threading

def echo(s, lock=threading.Lock()):
    time.sleep(1e-3*random.random())
    with lock: # comment it out, and run tox to detect error
        print(s)

for c in ['a b c '*10]*200:
    threading.Thread(target=echo, args=(c,)).start()
