from collections import Counter
userip=input("Enter the sentence")
uslist=userip.split()
di={}
mwords=sorted(uslist)
for w in mwords:
    di[w] = uslist.count(w)
print(di)
