num_words = 0

with open('3ip','r') as f:
    with open("3out", "w") as f1:
        lines=f.read().splitlines()
        print(lines)
        for line in lines:
            words = line.split()

            num_words = len(words)

            f1.write("{},{}\n".format(line,num_words))


