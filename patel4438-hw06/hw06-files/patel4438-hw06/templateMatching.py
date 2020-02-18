#Arpan patel
#1001554438

import skimage.feature as ss
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 


#function takes in images and converts them to grayscale 
def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    grayscale = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    plt.figure()
    plt.imshow(grayscale,cmap="gray")
    plt.show()
    
    return grayscale
            
def findImage(mainImage, template) :
        
        #sending the image to convert to grayscale
        main = rgb2gray(mpimg.imread(mainImage))
        
        temp = rgb2gray(mpimg.imread(template))
        
        #using the match_template fucntion to find
        #where template fits
        match = ss.match_template(main,temp)
        
        #getting row and col from the template location
        col = np.argmax(np.max(match, axis=1))
        
        row = np.argmax(np.max(match, axis=0))
        
        row_start = row
        col_start = col
        
        row_end = row + len(temp) 
        col_end = col + len(temp) 
        
        #setting where the template image fits to 0 so
        #it has a black square showing where it fits
        while row_start < row_end:
              col_start = col
              while col_start < col_end:
                   main[col_start][row_start] = 0
                   col_start+=1
              row_start+=1
               
        #plotting final result
        plt.figure()
        plt.imshow(main,cmap="gray")
        plt.show()
        
        #returing row and col values 
        return row,col
        #return result
        
#############  main  #############
# this function should be how your code knows the names of
#   the images to process
# it will return the coordinates of where the template best fits

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    r,c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))
