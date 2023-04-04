List_1 = [5,6,7,8]
List_2 = [11,22]
List_3 = [33,44]

output=[]

for i in List_1:
    if i==List_1[0]:
        output.extend(List_2)
    elif i==List_1[-1]:
        output.extend(List_3)
    elif i!=List_1 or i!=List_2:
        output.append(i)
    

print(output)