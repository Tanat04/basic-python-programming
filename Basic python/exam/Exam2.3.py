list1 =  [6, 1, 8, 2, 4, 0]
list2 = [0, 0, 0, 0, 0, 0]

sm =0
newLt = []

for i in range(len(list1)):
    if i == 0:
        newLt.append(list1[i])
        sm+=list1[i]
    else:
        sm+=list1[i]
        newLt.append(sm)

for i in range(len(list2)):
    print(f"list2[{i}] = {newLt[i]}")
