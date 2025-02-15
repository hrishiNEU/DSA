def pyramid(n):
    for i in range(1,n-1):
        print("")
        for j in range(0,i):
            print("*", end="")

pyramid(5)