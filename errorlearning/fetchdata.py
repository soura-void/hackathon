import csv
import datetime



def dataset() :
    datafile1 = open("../training.txt")
    datafile1reader = csv.reader(datafile1)
    x = []
    y = []
    z = []
    w = []
    i = 0
    for row in datafile1reader:
    	"""print(row[4])"""
    	if(i == 0):
           i = i+1
           continue
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
        w.append(row[4])

    print(x)
    print(y)
    return x, y, z, w

"""x.reverse()
y.reverse()"""

