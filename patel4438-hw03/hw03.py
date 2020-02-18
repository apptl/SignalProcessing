#Arpan Patel
import numpy as np 
import csv
import math

#pulse 0 and pulse 1 to compare 
pulse0 = np.ones( 10 )
u = pulse0/np.linalg.norm(pulse0)

pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
w = pulse1/np.linalg.norm(pulse1)

#read in the csv file
with open('data-communications.csv') as csvfile:
     readCSV = csv.reader(csvfile, delimiter=',')

     #print(type(readCSV))
     lowerlimit=0  
     upperlimit=10  
     bits = []
     index  = 0
     string = ""
      #for loop that reads entire file and stores the values in row
      #row then gets sliced in to 10 values at a time 
      #which are used to calculate the diffrence
     for row in readCSV:
   
         while( upperlimit <= len( row )):
            tenVal = row[ lowerlimit : upperlimit ]
            v = np.array( tenVal, dtype='float')

            cosThetaZero = np.dot( u, v )/np.linalg.norm( u )/np.linalg.norm( v )
            
            cosThetaOne = np.dot( w, v)/np.linalg.norm( w )/np.linalg.norm( v )
           
            if(abs( cosThetaZero )>abs( cosThetaOne )):
               bits.append( 0 )
            elif(abs( cosThetaOne )>abs( cosThetaZero )):
               bits.append( 1 )  

            upperlimit+=10
            lowerlimit+=10
            
#print(bytw)
#packing all the bits from matching together
byte = np.packbits( bits )

#combining all the bytes and converting to char as well as making it an entire string 
#so chars do not print on seperate lines
while( index<len( byte )):
   string = string + chr( byte[ index ])
   index+=1
print( string )
        
        
