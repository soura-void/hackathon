import csv
from os import listdir
from os.path import isfile, join
import dataset from fetchdata
 
wt_tilt = 0.45
wt_img = 0.3
wt_ldr = 0.25

with open("profit_large.csv", 'w+') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lis)

