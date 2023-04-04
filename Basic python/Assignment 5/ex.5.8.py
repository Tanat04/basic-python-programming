for i in range(1,10):
    print("Row number" , i,end=": ")
    if i % 2 == 1:
        for j in range(1,10):
            if j % 2 == 1 :
                print(" ",end = " ")
            else:
                print(j,end = " ")
    print()

print()
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")
print()

for i in range(1,10):
    print("Row number" , i,end=": ")
    if i == 1 or i == 5 or i == 9:
        for j in range(1,10):
            if j == 1 or j == 5 or j == 9:
                print(j,end = " ")
            else:
                print(" ",end = " ")
    print()

