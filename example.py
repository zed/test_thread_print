"""Run until empty line is found:

   $ while ! python example.py 2>&1|tee out|grep '^$';do echo -n .;done;cat out
"""
import random, sys, time
import threading

lock = threading.Lock()

def echo(s):
    time.sleep(1e-3*random.random())
    lock.acquire()
    try: print(s)
    finally:
        lock.release()

for c in '\t': # works due to `!space()` condition in 
               # http://hg.python.org/cpython/file/2.7/Python/ceval.c#l1775
    threading.Thread(target=echo, args=(c,)).start()
