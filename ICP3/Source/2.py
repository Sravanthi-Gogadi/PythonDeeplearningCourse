# Take the input from user
ip=input("Enter the sentence")
# reading the vowels as set
vowel=set("aeiouAEIOU")
count=0
for i in ip:
    if i in vowel:
        count= count+1
print("Total number of vowels {}".format(count))