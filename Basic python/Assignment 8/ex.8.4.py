num=int(input("Enter the amount of the number: "))
lt=[]
for n in range(num):
    numbers= int(input("Enter the number: "))
    lt.append(numbers)

for i in lt:
    if i == 13:
        pos=lt.index(13)
        pos+=1
        lt.remove(lt[pos])
        lt.remove(13)
    else:
        continue
print("The sum is: ",sum(lt))