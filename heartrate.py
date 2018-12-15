import mraa
import time
from timeit import default_timer as timer
import sys

class Counter:
    count = 0
    heart_rate = 72
    elapsed_time = 0

c = Counter()
#Assuming default heart rate as 72

def isr(gpio):
    c.heart_rate = (((60/c.heart_rate) + (timer() - c.elapsed_time)) / 2) * 60
    c.elapsed_time = timer()
    print(c.heart_rate)

try:
    x = mraa.Gpio(23)
    x.dir(mraa.DIR_IN)
    t = raw_input("Enter to start")
    c.elapsed_time = timer()
    x.isr(mraa.EDGE_RISING, isr, x)

    t = raw_input("Enter to stop")
    x.isrExit()
except ValueError as e:
    print(e)
