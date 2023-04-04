list_1 = [2,4,10]
list_2 = [1,5,10,20]

for i in list_2:
    for j in list_1:
        result=i*j
        if result< 100:
            print(i*j,end="\t")
        else:
            print("***",end="\t")
    print()

print("*<------------------------------>*")

for i in list_1:
    for j in list_2:
        result=i*j
        if result< 100:
            print(i*j,end="\t")
        else:
            print("***",end="\t")
    print()