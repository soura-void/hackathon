import time
import mraa

files = ['heartrate.txt', 'tilt.txt','light.txt']

## API to return average heartrate reading 
def read_heartrate():
    values = []
    f = open(files[0], "r+").read().splitlines()
    for lines in f:
        values.append(int(round(float(lines.strip()))))

    avg_val =  sum(values[-15:])/15
    if avg_val > 100:
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

## API to blink LED in case of danger 
def led_glow(x):
    a = mraa.Gpio(29)
    a.dir(mraa.DIR_OUT)
    for i in range x*4:
        a.write(1)
        time.sleep(0.1)
        a.write(0)
        time.sleep(0.1)


if __name__=='__main__':
    while True:
        h = read_heartrate()
        t = read_tilt()
        l = read_light()
        print t
        if t[0] == 1 or h == 1 or l[0] == 1:
            led()
        print(str(h) + "--" + str(t) + "--" + str(l))
        time.sleep(1)
