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

for c in ['abc'*10**6]*3:
    threading.Thread(target=echo, args=(c,)).start()
