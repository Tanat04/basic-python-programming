listA = [1, 3, 60, 73, 7, 88, 50, 13, 20, 98, 100, 2, 35, 40, 9]

list1 =[]
list2 =[]

for num in listA:
    if num <= 50:
        list1.append(num)
    else:
        list2.append(num)

list1.sort()
list2.sort()
print(f"list1 -> {list1}")
print(f"list2 -> {list2}")