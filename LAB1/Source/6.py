# import numpy library
import numpy as np
array = np.random.randint(20, size=15) #Generate 15 random numbers of range 0-20
print(array)
counts = np.bincount(array)  #bincount() counts no.of occurances of each value in an array of non-negative ints
print(np.argmax(counts)) #argmax(counts) prints the most frequent number




