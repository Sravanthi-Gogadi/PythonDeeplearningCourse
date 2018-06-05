#  Guess numbers
import random
prgmnum=random.randint(0,9)
usernum=int(input("Guess the number"))
print(prgmnum)
if(prgmnum==usernum):
    print("Vola!! You have a great guess")
elif(prgmnum>usernum):
    print("Your answer is low than required")
else:
    print("Your answer is greater than required")
