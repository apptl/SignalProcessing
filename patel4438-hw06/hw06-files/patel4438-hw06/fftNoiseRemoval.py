#Arpan patel
#1001554438

import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

#offset was picked by hovering over the graph
#and observing where the values start being almost
#o and then subtracted mid from there

def processFile(fn, offset) :
    #read in audio file
    data, samplerate = sf.read(fn)
    
    fig, ax = plt.subplots(1, 2)
    #plotting orginal data
    fil = np.fft.fft(data)
    
    #print(fil[23110])
    
    mid = (int)(len(fil) / 2)
    
    low = (int) (mid - offset)
    
    high = (int) (mid + offset)
    #print(mid)
    
    #first plot which has noise in the middle
    ax[0].plot(abs(fil))
    ax[0].set_title("fft")
    
    #removing noise 
    while(low<high):
        fil[low] = 0
        low+=1
     
    #plotting after pushing 0 to mid +- offset 
    ax[1].plot(abs(fil))
    ax[1].set_title("after removing noise")
    
    plt.tight_layout()
    plt.show()
    
    #saving the new clean music
    final = np.fft.ifft(fil)
    
    final = np.real(final)
    
    
    sf.write('cleanMusic.wav', final , samplerate)
    
    
    
    
##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav" 
    offset = 9588

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)







