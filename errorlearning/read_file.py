import time
import os

files = ['heartrate.txt', 'tilt.txt','light.txt']

HEART_RATE_THRESHOLD = 82

## API to return average heartrate reading 
def read_heartrate():
    values = []
    f = open(files[0], "r+").read().splitlines()
    for lines in f:
        values.append(int(round(float(lines.strip()))))

    avg_val =  sum(values[-15:])/15
    if avg_val > HEART_RATE_THRESHOLD:
        return 1
    else:
        return 0

## API to return tilt sensor reading 
def read_tilt():
    values = []
    f = open(files[1], "r+").read().splitlines()
    for lines in f:
        values.append(int(lines.strip()))

    return values[-1:][0]

## API to return ambient sensor reading
def read_light():
    values = []
    f = open(files[2], "r+").read().splitlines()
    for lines in f:
        values.append(int(lines.strip()))

    return values[-1:][0]

def led_glow(x):
    if x == 1: 
        os.system("python led.py 1")
    if x == 2: 
        os.system("python led.py 2")
    if x == 3: 
        os.system("python led.py 3")


if __name__=='__main__':
    while True:
        h = read_heartrate()
        t = read_tilt()
        l = read_light()
        print(str(h) + "--" + str(t) + "--" + str(l))
        time.sleep(1)
