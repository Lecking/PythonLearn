a=int(input("行数："))
for i in range(a):
    for j in range(i,2*a-1-i):
        print("*",end=" ")
    print()
    for k in range(0,i+1):
        print("  ",end="")