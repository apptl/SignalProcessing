#Arpan Patel
#1001554438

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def applyShelvingFilter(inName, outName, g, fc) :
    #file data and samplerate
    x, fs = sf.read(inName)    
     
    #variables as mentioned in the pdf given
    mu = pow(10,(g/20))
    
    theta = (2*np.pi) * (fc/fs)
    
    well = np.tan(theta/2)
    
    fig, ax = plt.subplots(1, 2)
    
    gamma = (1- (4/(1+mu)) * well)/ ( 1+ (4/(1+mu)) * well) 
    
    alpha = (1-gamma)/2
    
    #fft of original signal 
    fftorig = np.fft.fft(x)
    
    N = len(x)
    d = 1/fs
    
    
    xwell = np.fft.fftfreq(N,d)
   
    
    
    
    u = np.zeros(N)
    y = np.zeros(N)
    i = 0
    y[i] = x[i]
    u[i] = x[i] + gamma
    i += 1
    y[i] = 0
    u[i] = alpha*(x[i]+x[i-1]) + gamma*(u[i-1])
    i = 2
   #difference equation from the pdf given
    while i < N:
        u[i] = alpha*(x[i]+x[i-1]) + gamma*(u[i-1])
        y[i] = x[i] + ((mu-1) * u[i])
        i += 1
    #fft of new filtered signal
    fftnew = np.fft.fft(y)
    xwell = np.fft.fftfreq(N,d)
    
    #plot of original signal with N/4 values
    
    ax[0].plot(abs(xwell[0:(len(x)//4)]),abs(fftorig[0:(len(x)//4)]))
    #ax[0].set_ylim(0, (max( abs(np.max(fftorig)), abs(np.max(fftnew))) )+ 100 )
    ax[0].set_title("Original")
  
    #plot of new filtered signal with N/4 and Ylim set to max magnitude of 
    #both charts + 100
    ax[1].plot(abs(xwell[0:(len(x)//4)]),abs(fftnew[0:(len(x)//4)]))
    ax[1].set_ylim(0, (max( abs(np.max(fftorig)), abs(np.max(fftnew))) )+ 100 )
    ax[1].set_title("filtered")
    #print(max( abs(np.max(fftorig)), abs(np.max(fftnew))) )
    
    #ifft of signal to produce an output file
    final = np.fft.ifft(fftnew)
    final = np.real(final)
    
    #output file
    sf.write(outName, final , fs)
    
    plt.tight_layout()
    plt.show()
##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)







