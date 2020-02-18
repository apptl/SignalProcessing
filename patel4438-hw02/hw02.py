#Arpan patel
import numpy as np
import soundfile as sf

#Notes aquired from keyboard
notes = [52,52,59,59,61,61,59,59,57,57,56,56,54,54,56,52,59,59,57,57,56,56,54,54]
frequencies = []

#calculating frequencies for each note 
for keyNumber in notes:
  f = 440 * np.power(2, (keyNumber-49)/12)
  frequencies.append(f)
  #print(len(frequencies))
  #print(frequencies)

index = 0
vals = []

while(index < len(notes)):
  #"continous" signal creation
     signal = np.arange(0, 0.5, 1/8000)
     coswave = np.cos(2*(np.pi)*(frequencies[index])*(signal))
     #single sequence of values
     vals = np.concatenate((vals,coswave))
     index = index + 1

sf.write('twinkle.wav', vals, 8000)