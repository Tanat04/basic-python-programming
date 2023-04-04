def MoDuplicate(int_list):
 newli = []
 seen = set()
 for item in int_list:
    if item not in seen:
        seen.add(item)
        newli.append(item)
    else:
        if item % 2 ==1:
            seen.add(item*10)
            newli.append(item*10)
        else:
            seen.add(item*20)
            newli.append(item*20)

 print(li)
 return newli
li = [1,1,3,5,4,5,5,9,4,8,6]
print(li)
li = MoDuplicate(li)
print(li)