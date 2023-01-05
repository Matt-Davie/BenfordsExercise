import numpy as np
import csv 
import os
import sys

def main(input_file = 'BenfordTestData.csv'):
    """
    The main execute goes here
    Expects a file named: BenfordTestData.csv to be in the same
    diractory to be used if no argument is passed when running
    the script
    """
    #  Get system path of script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    #  Create absolute path of file
    input_path = script_dir + '\\' + input_file
    
    with open(input_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        #  Remove CSV header
        next(reader)

        data = np.array(list(reader))

        #  Get rid of index column
        data=data[:,1:]

        #  Get 1st entries
        for i in range(data.shape[1]):
            for j in range(data.shape[0]):
                data[j,i]=firstdigit(float(data[j,i]))


stats = {}
for i in items:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

# bonus
for i in sorted(stats, key=stats.get):
    print("%d×'%s'" % (stats[i], i))
