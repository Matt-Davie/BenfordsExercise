###  Notes  ###
#  load file
#  get 1st non-zero integer digits
#  count each
#  divide by sum(counts) to get %
#  print
#  display benfords ratios

#  assumptions: values can be floats - this means -ve, -1<x<1, including zero
#  decide how to handle -ve: make +ve
#  decide how to handle zero : return 0
#  decide how to handle -1<x<1 : return 1st non-zero integer

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

        #  Count
        unique, counts = np.unique(data.flatten(), return_counts=True)
        #  Trim zero as it is irrelevant for Benford's
        if int(unique[0])==0:
            counts=counts[1:]
        total_count=np.sum(counts)

        data_percentage=[(i/total_count)*100 for i in counts]
        #  1dp
        data_percentage=np.around(data_percentage,1)

        #  Predicted values
        benfords=[np.log10(1+1/i)*100 for i in range(1,10)]
        #  1dp
        benfords=np.around(benfords,1)

        #  Output data
        print(data_percentage)
        print(benfords)


def firstdigit(n):
    """
    Finding the first non-zero integer digit
    """
    if n<0:
        #  No more negatives
        n=n*(-1)
    if n==0:
        #  Return zero if zero - not much can be done here, we'll skip it later.
        return int(0) 
    if n<1:
        #  Skip '0.' then iterate
        for i in str(n)[2:]: 
            if int(i)>0:
                #  Return first non-zero for cases like 0.40
                return int(i) 
    else:
        #  Just that first digit
        return int(str(n)[0])

if __name__ == '__main__':
    """
    Run this first
    """
    csv_filename = ''
    # If there is an argument passed, store it
    try:
        csv_filename = sys.argv[1]
    except:
        pass

    # If the filename ends with csv, use it for Benford's Law
    # else use the default value
    if csv_filename.endswith('.csv'):
        main(csv_filename)
    else:
        main()