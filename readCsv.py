#This is the example of CSV File
import csv
with open('biostat.csv','r') as csv_file:
    f=csv.reader(csv_file)
    for fi in f:
        print(fi)
#you can modify this in to different way