import mraa
import time
import sys
## API to blink LED in case of danger 
def led():
    x =sys.argv[1]
    a = mraa.Gpio(29)
    a.dir(mraa.DIR_OUT)
    for i in range(int(x)*4):
        a.write(1)
        time.sleep(0.1)
        a.write(0)
        time.sleep(0.1)

led()
