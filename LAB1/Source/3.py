"""
 Given a list of n number, write a Python program to find triplets in the list which gives the sum of zero.
 Sample input:[1, 3, 6, 2, -1, 2, 8, -2, 9]Sample output:[(3, -1, -2)]

"""
triplets = []
inp = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in range(0, len(inp) - 2):

    for j in range(i + 1, len(inp)- 1):

        for k in range(j + 1, len(inp)):

            if (inp[i] + inp[j] + inp[k] == 0):
                if (inp[i], inp[j], inp[k]) not in triplets:
                    triplets.append((inp[i], inp[j], inp[k]))
print(triplets)