import mraa
import time
from timeit import default_timer as timer
import sys

class Counter:
    count = 0
    start = 0
c = Counter()
f = open("tilt.txt", "w+")

def isr(gpio):
    c.count += 1

try:
    x = mraa.Gpio(27)
    x.dir(mraa.DIR_IN)
    t = raw_input("Press enter to start")
    c.start = timer()
    x.isr(mraa.EDGE_BOTH, isr, x)

    while True:
        if timer() > (c.start + 1):
            c.start = timer()
            print(c.count)
            if c.count >= 37:
                print("Danger")
                f.write("1\n")
            else:
                print("No Danger Balle Balle")
                f.write("0\n")
            c.count = 0
        
    t = raw_input("Enter to stop")
    x.isrExit()
except ValueError as e:
    print(e)
