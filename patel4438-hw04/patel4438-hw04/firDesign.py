#Arpan Patel
import csv
import numpy as np
import matplotlib.pyplot as plt

index=0
orig_sginal = []
lowpass = []
highpass = []

# getting data from csv file to row and then converting them from string 
# to float and  saving as orig_signal list 
with open('data-filtering.csv') as csvfile:
     readCSV = csv.reader(csvfile, delimiter=',')
     for row in readCSV:
          #print(len(row))
          while(index<len(row)):
              use = float(row[index])
              orig_sginal.append(use)
              index+=1
L = 21
M = L-1
fc = 50
fs = len(row)
ft = fc/fs
i=0
Muse = M/2

# getting filter weights for Lowpass filter
while(i < M):
              if(i==Muse):
                  wl = 2*ft
              else: 
                  temp = np.sin(2*np.pi*ft*(i-Muse))
                  wl = temp / (np.pi*(i-Muse))
              #print(wl)
              #print(i, "weight is " , wl)
              lowpass.append(wl)
              i+=1
i=0
fc = 280
ft = fc/fs
# getting filter weights for Highpass filter
while(i < M):
              if(i==Muse):
                  wh = 1 - 2*ft
              else: 
                  temp2 = np.negative(np.sin(2*np.pi*ft*(i-Muse)))
                  wh = temp2 / (np.pi*(i-Muse))
              #print(wh)
              #print(i, "weight is " , wl)
              highpass.append(wh)
              i+=1
            
"""
fig = plt.figure()
wel = plt.subplot(3,1,1)
plt.plot(orig_sginal)
nt = plt.subplot(3,1,2)
plt.plot(np.cos(2*np.pi*4*x))
plt.subplot(3,1,3)
plt.plot(low)
plt.show()
"""
# applying lowpass filter to original data by convolve
low = np.convolve(orig_sginal,lowpass)

# applying highpass filter to original data by convolve
high = np.convolve(orig_sginal,highpass)

# generating 4 Hz signal
x = np.arange(0, 1, (1/fs))
fourhz = np.cos(2*np.pi*4*x)

# generating 330 Hz signal
x = np.arange(0, 1, (1/fs))
tthz = np.cos(2*np.pi*330*x)

# plotting original signal, 4 Hz signal and 
# Lowpss filter application as subplots

fig, ax = plt.subplots(3, 1)
ax[0].plot(orig_sginal)
ax[0].set_title("Original Signal")
ax[1].plot(fourhz)
ax[1].set_title("4 Hz Signal")
ax[2].plot(low)
ax[2].set_title("Lowpass filter")
plt.tight_layout()
plt.show()

# plotting original signal, 330 Hz signal and 
# Highpass filter application as subplots 
# making sure to slice list in first 100 values
# so it is easier to see

fig, ax = plt.subplots(3, 1)
ax[0].plot(orig_sginal[0:100])
ax[0].set_title("Original Signal")
ax[1].plot(tthz[0:100])
ax[1].set_title("330 Hz Signal")
ax[2].plot(high[0:100])
ax[2].set_title("Highpass filter")
plt.tight_layout()
plt.show()