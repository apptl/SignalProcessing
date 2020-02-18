import numpy as np 
import csv
import math

with open('.csv') as csvfile:
     readCSV = csv.reader(csvfile, delimiter=',')
     

m = 20
ft = 50/2000
index = 0
while(index<(m+1)):
    if(index == (m/2)):
        print(ft * 2)
    else:
        wt = np.sin(2*(np.pi)*ft*(index-(m/2))) 
        wt2 =  np.pi*(index-(m/2))
        print(wt/wt2)
    index+=1