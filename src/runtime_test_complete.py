import time, machine

def test_f():
    l = 10000000
    s = 0
    for i in range(l):
        s = s + 1
    return s

def runtime(func):
     a = time.time()
     b = func()
     print(time.time() - a)
     return b

cpu_speeds = [160000000, 240000000]

for speed in cpu_speeds:
    machine.freq(speed)
    runtime(test_f)