"""Run until empty line is found:

   $ while ! python example.py 2>&1|tee out|grep '^$';do echo -n .;done;cat out
"""
from __future__ import print_function
import random, sys, time
import threading

lock = threading.Lock()

def echo(s):
    time.sleep(1e-3*random.random())
    lock.acquire()
    try: 
        if isinstance(s, int): # py3k
            sys.stdout.write(chr(s))
        else:
            sys.stdout.write(s)
        sys.stdout.write('\n')
    finally:
        lock.release()


for c in 'abc'.encode('ascii'):
    threading.Thread(target=echo, args=(c,)).start()
