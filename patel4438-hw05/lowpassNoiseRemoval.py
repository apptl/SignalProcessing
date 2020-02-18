#Arpan patel
#1001554438

import numpy as np 
from scipy.signal import freqz
import matplotlib.pyplot as plt
import soundfile as sf

#reading the soundfile 
data, samplerate = sf.read('P_9_2.wav')


#setting up filter Length and cut off frequency
fc = 7500
L = 101 
M = L - 1 
fs = samplerate
ft = fc/fs
hamming_coefficients = []
lowpass_coefficients = []

#Function to get lowpass filter coefficiants
def lowpass_coff():
    i=0
    while(i < M):
        if(i==(M/2)):
            weights = 2*ft
        else: 
            temp = np.sin(2*np.pi*ft*(i-(M/2)))
            weights = temp / (np.pi*(i-(M/2)))
        lowpass_coefficients.append(weights)
        i+=1
     
#Function to get hamming window coefficiants     
def hamming_coff():
    i=0
    while (i< M):
      hamming_weights = .54 - .46 * (np.cos((2 * np.pi * i) / M))
      hamming_coefficients.append(hamming_weights)
      i+=1

#function calls to load data in two main lists
lowpass_coff()
hamming_coff()
print(lowpass_coefficients)
print(len(lowpass_coefficients))
#multiplying lowpass coefficiants with hamming window coefficiants 
filter_coff = np.multiply(lowpass_coefficients,hamming_coefficients)

#freqency response of just lowpass signal
x,y = freqz(lowpass_coefficients,1)
plt.plot(x,abs(y))


#frequency response of lowpass with hamming window
w,z = freqz(filter_coff,1)
plt.plot(w,abs(z))

plt.legend(['Original', 'Windowed'])
plt.show()

#applying the newly created filter to orginal data
final_filter = np.convolve(data,filter_coff)

#saving data as audio file with same samplerate
sf.write('cleanMusic.wav', final_filter , samplerate)

