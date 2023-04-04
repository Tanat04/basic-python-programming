def MergeandSort(list1,list2):
    list1.extend(list2)
    list1.sort(reverse=True)
    return list1

list1 = [1,4,6]
list2 = [3,7,9]

print(f"Outlist = {MergeandSort(list1,list2)}")
