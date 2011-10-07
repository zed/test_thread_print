"""Run until empty line is found:

   $ while ! python example.py |tee out |grep '^$';do echo -n . ;done; cat out
"""
import random, sys, time
import threading

lock = threading.Lock()

def echo(s):
    time.sleep(1e-4*random.random())
    with lock:
        print s

for line in 'abc':
    threading.Thread(target=echo, args=(line,)).start()
