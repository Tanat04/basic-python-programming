inStr=input("Enter a string: ")
cDigit=int(input("Enter a digit: "))
print()
num=""
lt=[]
count=0

for i in inStr:
    num+=i

num2=num
if int(num2)<9:
    print("No pairs at all!!")
else:
    while int(num2)>9:
        digit=int(num2)%100
        lt.append(digit)
        num2=int(num2)//10

    for n in lt:
        n=int(n)
        if str(cDigit) in str(n):
            count+=1

    if count==len(lt) and count!=0:
        print(f"The string DOES contain {cDigit} in every adjacent digit in input string.")
    if count==0:
        print("No pairs at all!!")
    elif len(lt) > count>=1:
        print(f"This string DOES NOT contain {cDigit} in every adjacent digit in input string.")