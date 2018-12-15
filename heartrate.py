import mraa
import time
from timeit import default_timer as timer
import sys

class Counter:
    count = 0
    temp = 1
    #Assuming default heart rate as 72
    heart_rate = 72
    elapsed_time = 0
    current_time = 0

c = Counter()
f = open("heartrate.txt", "w+")

def isr(gpio):
    c.current_time = timer()
    diff = c.current_time - c.elapsed_time
    if diff < 0.4512 or diff > 1.1451:
        c.elapsed_time = timer()
        print("Heart Rate: " + str(c.heart_rate))
        return
    c.temp = (((60/c.heart_rate) + (c.current_time - c.elapsed_time)) / 2)
    c.heart_rate = 60/c.temp
    c.elapsed_time = timer()
    print("Heart Rate: " + str(c.heart_rate))
    f.write(str(c.heart_rate) + "\n")

try:
    x = mraa.Gpio(23)
    x.dir(mraa.DIR_IN)
    t = raw_input("Enter to start")
    x.isr(mraa.EDGE_RISING, isr, x)
    c.elapsed_time = timer()

    t = raw_input("Enter to stop")
    x.isrExit()
except ValueError as e:
    print(e)
