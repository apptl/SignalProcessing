from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.signal import spectrogram

def processTones(name, L, fs, samplesPerTone) :
    with open(name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        
        for row in readCSV:
            data = np.array(row,dtype='float')
    
    
    index=0
    freq = [697,770,852,941,1209,1336,1277]
    coff=np.empty((len(freq),L))
    samples = 0
    samplesmax = 4000
    plt.figure(1)
    for i in freq:
        k=0
        while(k<L):
            coff[index][k] = (2/L)*(np.cos(2*np.pi*i*k/fs))
            k+=1
        x,y = freqz(coff[index],1) 
        
        plt.plot(x*1000,abs(y))
        
        index+=1
    mean = []
    mean1 = mean2 = 0
   
    count = 0
    number = []
    while(samples < len(data))  :      
        for i in coff:
            temp = (np.convolve(data[samples:samplesmax], i))
            mean.append(np.mean(temp**2))
        for k in range(0,len(mean)):
            if(mean[k] > mean1):
                mean1 = mean[k]
                i1=k
        for g in range(0,len(mean)):
            if(mean[g] > mean2 and mean[g] < mean1):
                mean2 = mean[g]
                i2=g
        
        mean.clear()
        
        count+=1
        
        if((freq[i1] == 1209 and freq[i2] == 697) or (freq[i2] == 1209 and freq[i1] == 697)):
            number.append("1")
        elif((freq[i1] == 1336 and freq[i2] == 697) or (freq[i2] == 1336 and freq[i1] == 697)):
            number.append("2")
        elif((freq[i1] == 1477 and freq[i2] == 697) or (freq[i2] == 1477 and freq[i1] == 697)):
            number.append("3")
        elif((freq[i1] == 1209 and freq[i2] == 770) or (freq[i2] == 1209 and freq[i1] == 770)):
            number.append("4")
        elif((freq[i1] == 1336 and freq[i2] == 770) or (freq[i2] == 1336 and freq[i1] == 770)):
            number.append("5")
        elif((freq[i1] == 1477 and freq[i2] == 770) or (freq[i2] == 1477 and freq[i1] == 770)):
            number.append("6")
        elif((freq[i1] == 1209 and freq[i2] == 852) or (freq[i2] == 1209 and freq[i1] == 852)):
            number.append("7")
        elif((freq[i1] == 1336 and freq[i2] == 852) or (freq[i2] == 1336 and freq[i1] == 852)):
            number.append("8")
        elif((freq[i1] == 1477 and freq[i2] == 852) or (freq[i2] == 1477 and freq[i1] == 852)):
            number.append("9")
        elif((freq[i1] == 1209 and freq[i2] == 941) or (freq[i2] == 1209 and freq[i1] == 941)):
            number.append("*")
        elif((freq[i1] == 1336 and freq[i2] == 941) or (freq[i2] == 1336 and freq[i1] == 941)):
            number.append("0")
        elif((freq[i1] == 1477 and freq[i2] == 941) or (freq[i2] == 1477 and freq[i1] == 941)):
            number.append("#")
        
        mean1 = mean2 = i1 = i2 = 0
        samples+=4000
        samplesmax+=4000
    
    index=0
    string = ""
    while( index<len( number )):
        string = string + number[ index ]
        index+=1      
    plt.figure(2)
    f, t, Sxx = spectrogram(data, fs)
    plt.pcolormesh(t,np.fft.fftshift(f),np.fft.fftshift(Sxx,axes=0))
    plt.show()
    return string
         
    
     
    
#############  main  #############
if __name__ == "__main__":
    filename = "tones-8675309.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone, 
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)
    
    print(phoneNumber)
