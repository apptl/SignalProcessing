
import numpy as np 
from scipy import signal
import cmath


a = [1,2,1,2]
b = [3,0,-1,-4]

c=np.fft.fft(a)
print("\nx1[k]",c)
d=np.fft.fft(b)
print("\nx2[k]", d)
final = np.add(a,b)
ffft = np.fft.fft(final)
print("\nfft of a + b",ffft)
final2 = c + d
print("\nx1[k] + x2[k]",final2)

print(" ")

q2a = np.convolve(a,b)
print("\nq2a",q2a)
q2b = np.multiply(c,d)
print("\nq2b",q2b)
q2c = np.fft.ifft(q2b)
print("\nq2c",q2c)

xz1 = [1,2,1,2,0,0,0]

xz2 = [3,0,-1,4,0,0,0]

XZ1 = np.fft.fft(xz1)
print("e",XZ1)
XZ2 = np.fft.fft(xz2)
print("e2",XZ2)

XZK = np.multiply(XZ1,XZ2)
print("f",XZK)
inxzk = np.fft.ifft(XZK)
print("ifft g",inxzk)

"""
fs = 4000
L = 64

"""

