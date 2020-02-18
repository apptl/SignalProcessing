"""
   Arpan patel
"""


import numpy as np
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA, PCA
import matplotlib.pyplot as plt


def unmixAudio(leftName, rightName) :
    
    #inout audio
    data, samplerate = sf.read(leftName)
    data2, samplerate2 = sf.read(rightName)
   
    s1 = data
    s2 = data2
    
    
    S = np.c_[s1 , s2]

    #source seperation
    ica = FastICA(n_components=2)
    S_ = ica.fit_transform(S)  # Reconstruct signals
    
    
    fig, ax = plt.subplots(4, 1)
    
    #plots
    ax[0].plot(S[:,0])
    ax[0].set_title("darinSiren0")
    
    ax[1].plot(S[:,1])
    ax[1].set_title("darinSiren1")
    
    ax[2].plot(S_[:,0])
    ax[2].set_title("unmixed0")
    
    ax[3].plot(S_[:,1])
    ax[3].set_title("unmixed1")
   
    plt.tight_layout()
    plt.show()
    
    #output audios
    sf.write("unmixed0.wav",((S_[:,0])*10),samplerate)
    sf.write("unmixed1.wav",((S_[:,1])*10),samplerate2)
    
    plt.show()
    
    

###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
