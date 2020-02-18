import numpy as np
import soundfile as sf

def main():
 
 nodes = [52,52,59,59,61,61,59,59,57,57,56,56,54,54,56,52,59,59,57,57,56,56,54,54]

 frequencies = []

 for keyNumber in nodes:
  frequency = 440*np.power(2, (keyNumber-49)/12)
  frequencies.append(frequency)
  print(len(frequencies))
  print(frequencies)

 index = 0
 signals = []
 while(index < len(nodes)):
     signal = np.arange(0, 0.5, 1/8000)
     s_wave = np.cos(2*np.pi*frequencies[index]*signal)
     signals = np.concatenate((signals, s_wave))
     index = index + 1
 sf.write('twinkle.wav', signals, 8000)
main()
