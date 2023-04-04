myInt=int(input("Number: "))

for i in range(myInt,0,-1):
    if i % 2 == 0:
        print(i-2)
    else:
        print(i+1)
