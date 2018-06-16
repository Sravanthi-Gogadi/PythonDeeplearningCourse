"""
Using NumPy create random vector of size 15 having only Integers in the range 0-20.
Write a program to find the most frequent item/value in the vector list.
Sample input:[1,2,16,14,6,5,9,9,20,19,18]
Sample output:Most frequent item in the list is 9
"""
import numpy as np
array = np.random.randint(20, size=15)
print(array)
counts = np.bincount(array)
print(np.argmax(counts))

