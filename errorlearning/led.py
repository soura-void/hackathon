import mraa
import time

## API to blink LED in case of danger 
def led():
    a = mraa.Gpio(29)
    a.dir(mraa.DIR_OUT)
    for i in range(10):
        a.write(1)
        time.sleep(0.1)
        a.write(0)
        time.sleep(0.1)

led()
