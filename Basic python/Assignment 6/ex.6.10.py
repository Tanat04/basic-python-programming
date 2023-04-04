n=input("Input string: ")
count=0
for i in n:
    if i.isdigit():
        count+=1
if count>0:
    print(f"There are {count} digits in the string")
else:
    print("There is no digit at all!")