"""
    Arpan patel
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import math

def getData(fn) :
    well = []
    tmp = []
    #read data from csv
    with open(fn) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        count = 0
        for row in csv_reader:
            if(count!=0):
                well.append(row)
                line_count+=1
            count+=1
    #string to float conversion
    for i in well:
        tmp.append(float(i[12]))  
   
    return tmp,line_count

def analysis(temps, tfft, N) :
    #analysis
    print("i. Samplerate is 24 Samples/Day = 1 Sample/Hour","\n")
     
    new = []
    for i in range(0,len(tfft)):
        temp = (abs(tfft[i]))
        new.append(temp)
        
    index1 = np.argmax(new)
    max1 = max(new)
    
    max2 = 0
    for i in range(0,len(new)):
        if(new[i]>max2 and new[i]<max1):
            max2 = new[i]
            index2 = i
            
    max3 = 0
    for i in range(0,len(new)):
        if(new[i]>max3 and new[i] <= max2 and i!=index2):
            max3 = new[i]
            index3 = i
            
    new = np.asarray(new)
    fs = 24 #samples/day
    N = len(new)
    
    print("ii. Fundamental Freqency(Fs/N): ",fs/N,"Hz\n")
    print("iii. Index of first largest magnitude: ",index1,"\n")
    print("iv. Index of second largest magnitude: ",index2,"\n")
    print("v. Index of third largest magnitude: ",index3,"\n")
    
def plotTemps(t, tfft, N) :
    #plots
    plt.plot(t[0:24])
    plt.title("24 Hours")
    plt.xlabel("Hours")
    plt.show()
    
    plt.plot(t[0:(24*7)])
    plt.title("7 Days")
    plt.xlabel("Days")
    plt.show()
    
    plt.plot(t)
    plt.title("365 Days")
    plt.xlabel("Days")
    plt.show()
    
    
    plt.plot(abs(tfft))
    plt.xlabel("Days")
    plt.title("DFT")
    plt.show()
    
    well = []
    for i in tfft:
       well.append(math.log10(abs(i)))
    plt.plot(well)
    plt.title("Log")
    plt.show()
   
    

    
##################  main  ##################
#   DO NOT CHANGE THIS
fn = "weather.csv"

#  temps = list or ndarray of temperature values
#  N = number of elements in temps

temps, N = getData(fn)

#tfft = DFT coefficents of temps
tfft = np.fft.fft(temps)

analysis(temps, tfft, N)
plotTemps(temps, tfft, N)
