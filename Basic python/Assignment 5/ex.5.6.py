a=int(input("Enter a value for a: "))
b=int(input("Enter a value for b: "))

if a < b:
    for i in range(a,b+1):
        if i % 10 == 3 or i % 10 == 7:
            print("*",end=" ")
        else:
            print(i,end=" ")
else:
    print("Error!! The value of a must be less than b.")
