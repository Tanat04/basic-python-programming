n=int(input("n: "))

for j in range(1,n+1):
    space=" "
    for a in range(n-j):
        print(space,end="")
    for i in range(j):
        print("* ",end="")
    print()

for j in range(1,n):
    space=" "
    for a in range(j):
        print(space,end="")
    for i in range(n-j):
        print("* ",end="")
    print()
        
    
