#Arpan Patel
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from scipy import ndimage

def justprint(filename,name):
    plt.figure()
    img = mpimg.imread(filename)
    plt.imshow(img,cmap='Greys_r')
    plt.title(name)

def lowpass(filename,name):
    array = [.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]
    plt.figure()
    img = mpimg.imread(filename) 
    img2 = []
    for i in img:
        img2.append(np.convolve(i,array))
    plt.imshow(img2,cmap='Greys_r') 
    plt.title(name + " Lowpass")
    
def highpass(filename,name):
    array = [1,-1]
    plt.figure()
    img = mpimg.imread(filename) 
    img2 = []
    for i in img:
        img2.append(np.convolve(i,array))
    plt.imshow(img2,cmap='Greys_r') 
    plt.title(name + " Highpass")
    
#array of .1s to convolve
#convolving each picture with lowpass
#each pics row is convolved with .1s array
    
filenames = ["boat.512.tiff","clock-5.1.12.tiff",
             "man-5.3.01.tiff","tank-7.1.07.tiff"]

names = ["boat","clock","man","tank"]

i=0
while(i<len(filenames)):
    justprint(filenames[i],names[i])  
    i+=1
i=0
while(i<len(filenames)):
    lowpass(filenames[i],names[i])  
    i+=1
i=0
while(i<len(filenames)):
    highpass(filenames[i],names[i])  
    i+=1
    

justprint("darinGrayNoise.jpg","darin")
lowpass("darinGrayNoise.jpg","darin") 

plt.figure()
img = mpimg.imread("darinGrayNoise.jpg") 
outputImage = ndimage.median_filter(img, 5)
plt.imshow(outputImage,cmap='Greys_r')

