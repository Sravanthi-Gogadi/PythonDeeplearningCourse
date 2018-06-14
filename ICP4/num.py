# import the numpy library
import numpy as np
# Define the range of the matrix and reshape them
ip=np.arange(100).reshape(10,10)
# print the matrix
print(ip)
for i in range(10):
 # print the max and min values of each row in the numpy array
    print(" The min and max of {}th row are {} and {} ".format(i, min(ip[i]),max(ip[i])))
