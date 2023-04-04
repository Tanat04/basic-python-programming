for i in range (1,10):
    for j in range(1,10):
        result=i*j
        if result% 2 ==0:
            print("%2d"%(result),end="  ")
        else:
            print("--",end="  ")
    print()

print()
print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")
print()

for i in range (1,10):
    for j in range(1,10):
        result=i*j
        if (result%10)%2 == 0 and (result//10)%2==0:
            print("%2d"%(result),end="  ")
        else:
            print("--",end="  ")
    print()
