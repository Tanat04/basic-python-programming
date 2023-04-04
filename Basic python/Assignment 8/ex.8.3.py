List_1 = [3, 4]
List_2 = [3,6,7,4]
count=0
if len(List_1) <= len(List_2):
    for i in range(len(List_1)):
        if List_1[i] in List_2:
            count+=1
    if count==len(List_1):
        print("“Yes List_1 is a subset of List_2")
    else:
        print("“No List_1 is not a subset of List_2")
else:
    for i in range(len(List_2)):
        if List_2[i] in List_1:
            count+=1
    if count==len(List_2):
        print("“Yes List_2 is a subset of List_1")
    else:
        print("“No List_2 is not a subset of List_1") 