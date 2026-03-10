with open("input01.txt") as f:
    for line in f:
        if line.split()[0]=="Rectangle":
            a,b=map(int,line.split()[1:])
            print(a,b)