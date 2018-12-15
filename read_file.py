import time

files = ['heartrate.txt', 'tilt.txt']

def read_heartrate():
    values = []
    f = open(files[0], "r+").read().splitlines()
    for lines in f:
        print lines
        values.append(int(round(float(lines.strip()))))

    avg_val =  sum(values[-15:])/15
    if avg_val > 100:
        return 1
    else:
        return 0

def read_tilt():
    values = []
    f = open(files[1], "r+").read().splitlines()
    for lines in f:
        values.append(int(lines.strip()))

    return values[-1:]

if __name__=='__main__':
    while True:
        h = read_heartrate()
        t = read_tilt()
        print(str(h) + "--" + str(t))
        time.sleep(1)
