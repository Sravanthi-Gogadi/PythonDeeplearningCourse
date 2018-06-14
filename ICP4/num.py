# import the numpy library
import numpy as np
# Take the size of the input
imp=int(input("Enter the size of matrix"))
# Define the range of the matrix and reshape them
ip=np.arange(imp*imp).reshape(imp,imp)
print(ip)
for i in range(imp):
 # print the max and min values of each row in the numpy array
 print(" The min and max of {}th row are {} and {} ".format(i, min(ip[i]),max(ip[i])))
