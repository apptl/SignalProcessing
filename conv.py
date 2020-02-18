import numpy as np 


a = [0,1/4,2/4,3/4,1,3/4,1,3/4,2/4,1/4]
b = [1/4,1/4,1/4,1/4]

c = np.convolve(a,b)
for i in c:
    print(i.as_integer_ratio())