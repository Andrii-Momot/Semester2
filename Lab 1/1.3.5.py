with open("input.txt") as f:
    for line in f:
        #a=int(line.split()[0])
        #b=int(line.split()[1])
        a,b=map(int,line.split())
        print(a*b)