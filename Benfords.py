###Steps###
#load file
#get 1st non-zero integer digits
#count each
#divide by sum(counts) to get %
#print
#display benfords ratios

#assumptions: values can be floats - this means -ve, -1<x<1, including zero
#decide how to handle -ve: make +ve
#decide how to handle zero : return 0
#decide how to handle -1<x<1 : return 1st non-zero integer

import numpy as np
import csv

inputpath = 'BenfordTestData.csv'

def firstdigit(n): #finding the first non-zero integer digit
    if n<0:
        n=n*(-1) #no more negatives
    if n==0:
        return int(0) #return zero if zero - not much can be done here, we'll skip it later.
    if n<1:
        for i in str(n)[2:]: #skip '0.' then iterate
            if int(i)>0:
                return int(i) #return first non-zero for cases like 0.40
    else:
        return int(str(n)[0]) #just that first digit

#load this file
with open(inputpath, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader))

    #get rid of index column
    data=data[:,1:]

    #get 1st entries
    for i in range(data.shape[1]):
        for j in range(data.shape[0]):
            data[j,i]=firstdigit(float(data[j,i]))

    #now to count
    unique, counts = np.unique(data.flatten(), return_counts=True)
    if int(unique[0])==0: #trim zero as it is irrelevant for Benford's
        counts=counts[1:]
    total_count=np.sum(counts)

    data_percentage=[(i/total_count)*100 for i in counts]
    data_percentage=np.around(data_percentage,1) #1dp

    benfords=[np.log10(1+1/i)*100 for i in range(1,10)] #predicted values
    benfords=np.around(benfords,1) #1dp

    print(data_percentage)
    print(benfords)
