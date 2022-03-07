import time

def runtime(func):
     a = time.time()
     b = func()
     print(time.time() - a)
     return b