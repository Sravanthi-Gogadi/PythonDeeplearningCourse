# Importing math package
import math
# Take input from user
inp = input("Enter your sentence: ")
mywords = inp.split()     #splitting the sentence into a list of words
mid_index = int(math.floor((len(mywords)-1)/2)) #Finding the mid index

print(" The middle word is " ,mywords[mid_index]) #printing the middle word
longest =" "
reversed = " "
for i in mywords:
    reversed = reversed + i[::-1] + " "  #reversing every word of the list
    if len(i) > len(longest):
        longest = i    #finding the longest word
print(" The longest word is:" +longest)
print(" The reversed words n the sentence are:" +reversed) #printing the reversed words


