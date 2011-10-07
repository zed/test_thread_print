"""Run until empty line is found:

   $ while ! python example.py 2>&1|tee out|grep '^$';do echo -n .;done;cat out
"""
import random, sys, time
import threading

lock = threading.Lock()

def echo(s):
    time.sleep(1e-3*random.random())
    with lock:
        if isinstance(s, int): # py3k
            sys.stdout.buffer.write(bytes(s))
        else:
            sys.stdout.write(s)
        sys.stdout.flush()

for c in 'abc'.encode('ascii'):
    threading.Thread(target=echo, args=(c,)).start()
