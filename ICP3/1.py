# Take input from user
userip=input("Enter the sentence")
# Split the sentence into words
uslist=userip.split()
# Declare a dictionary
di={}
# Sorted the words in the dictionary
mwords=sorted(uslist)
for w in mwords:
    di[w] = uslist.count(w)
# Print the dictionary where keys are words and values are count of words
print(di)
