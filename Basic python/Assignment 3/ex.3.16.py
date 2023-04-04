n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
n4=int(input("Enter the four number: "))

Sum= n1+ n2+ n3+ n4

if Sum > 0 :
    print(f"The sum is: {Sum}")
    if Sum % 2 == 0 :
        print("Positive Even")
    else :
        print("Positive odd")

if Sum < 0 :
    print(f"The sum is: {Sum}")
    if Sum % 2 == 0 :
        print("Negative Even")
    else :
        print("Negative odd")

if Sum == 0 :
    print(f"The sum is: {Sum}")
    
