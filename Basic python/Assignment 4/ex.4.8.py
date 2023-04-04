n=int(input("Enter number of real numbers: "))

number= 1
firstHigh=-999999999
secondHigh=-999999999

while number<= n:
    num=float(input(f"Number#{number}: "))
    if num > firstHigh:
        secondHigh= firstHigh
        firstHigh= num  
    elif num <secondHigh:
        secondHigh = num
        
    number += 1

print()
if firstHigh != -999999999 :
    print(f"The first highest number is  {firstHigh}")
else:
    print(f"There is no first highest number")

if secondHigh != -999999999:
    print(f"The second highest number is  {secondHigh}")
else:
    print(f"There is no second highest number")


    

    
