#Arpan Patel
#1001554438

import numpy as np
import matplotlib.pyplot as plt
import csv


def applyNotch(fs, dataFile) :
    #data is stored in to an array
    data = []
    with open(dataFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data = np.array(row,dtype='float')
    
    #variables for the filter
    f = 17
    w = 2 * np.pi * (f/fs)
    N = len(data)

    x = data
    
    #filter using the difference equation from part 1 of Hw
    #((1.874*np.cos(w)*output[i-1]) - (.8783*output[i-2]) + (data[i]) - (2*np.cos(w) * data[i-1]) + data[i-2])
    y = []
    i = 0
    y.append(x[i])
    i += 1
    y.append( 1.874 * np.cos(w)*y[i-1] + x[i] - 2 * np.cos(w) * x[i-1])
    i = 2
    
    while i < N+100 :
        
        if(i > (N-1)):
            y.append(1.874*np.cos(w)*y[i-1] - .8783*y[i-2])
        else:
            y.append((1.874*np.cos(w)*y[i-1]) - (.8783*y[i-2]) + x[i] - (2 * np.cos(w) * x[i-1]) + x[i-2])
            
            #print(np.cos(w))
        i += 1 
    
    #plotting orginal signal
    plt.figure(1)
    plt.plot(data)
    plt.xlim([-25,625])
    plt.title("Original signal")
    
    plt.show()
    
    #plotting the filtered signal
    plt.figure(2)
    plt.plot(y)
    plt.ylim([-2.25,2.25])
    plt.title("Filtered signal")
    
    plt.show()
    
    #creating 10 and 33hz signals
   
    x = np.arange(0,N, (1/fs))
    tenhz = np.cos(2*np.pi*10*x)
    
    thirtythreehz = np.cos(2*np.pi*33*x)
    
    #element wise addition of signals and plot of combined signal
    plt.figure(3)
    addedsig = np.add(tenhz,thirtythreehz)
    addedsig = addedsig[0:500]
    plt.plot(addedsig)
    plt.xlim([-25,625])
    plt.title("10hz + 33hz")
    
    plt.show()

############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)









