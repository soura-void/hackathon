files = ['heartrate.txt', 'tilt.txt']

def read_heartrate():
    values = []
    with open(files[0], "r+") as f:
        values.append(int(round(float(f.readline().strip()))))

    avg_val =  sum(values[-15:])/15
    if avg_val > 100:
        return 1
    else:
        return 0

def read_tilt():
    vlaues = []
    with open(file[1], "r+") as f:
        values.append(int(round(float(f.readline().strip()))))

    return values[-1:]


