words_list=["PHP", "Exercises", "Backend"]
word_len=[]
finallist=[]
for i in words_list:
    x=len(i)
    word_len.append(x)
    finallist.append((len(i),i))
print(word_len)
sorted(finallist)
print(finallist)
print(finallist[-1])
