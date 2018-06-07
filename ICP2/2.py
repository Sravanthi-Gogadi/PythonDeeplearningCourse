with open('2ip') as f:
    content = f.read().splitlines()
    with open("2out", "w") as f1:
        for i in content:
            st =str(len(i))
            f1.writelines("{},{} \n".format(i,st))