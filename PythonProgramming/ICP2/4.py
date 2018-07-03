inp=int(input("Enter the size of game board: "));
def dashline():
    print(" --- "*inp);
def vertline():
    x=inp+1
    print("|    "*x)
for i in range(inp):
    dashline()
    vertline()
dashline()