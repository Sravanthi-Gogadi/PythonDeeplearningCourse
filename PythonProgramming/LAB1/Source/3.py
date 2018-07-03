# define a list named triplets
triplets = []
# Take input from the input
inp = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in range(0, len(inp) - 2): #ranging from the first element to the last but 3rd element

    for j in range(i + 1, len(inp)- 1): #ranging from the first element to the last but 2nd element

        for k in range(j + 1, len(inp)): #ranging from the first element to the last but one element

            if (inp[i] + inp[j] + inp[k] == 0):
                if (inp[i], inp[j], inp[k]) not in triplets:
                    triplets.append((inp[i], inp[j], inp[k])) # if the sum is 0 and the triplet is not in list, add it

print("Triplets are" ,triplets)
