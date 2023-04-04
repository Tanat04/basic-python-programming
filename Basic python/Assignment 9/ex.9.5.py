def OnlyOdd(intList): 
    ltOdd=[] 
    countOdd=0 
    for i in intList: 
        if int(i) % 2 == 1: 
            ltOdd.append(i) 
            countOdd+=1 
    return countOdd,ltOdd 

def OnlyEven(intList): 
    ltEven= [] 
    countEven=0 
    for i in intList: 
        if int(i) % 2 == 0: 
            ltEven.append(i) 
            countEven+=1 
    return countEven,ltEven 
    
num=input("Input = ").split()

countodd,ltOdd=OnlyOdd(num) 
countEven,ltEven=OnlyEven(num) 

if countEven > countodd: 
    print(f"Output = {ltEven}") 
else: 
    print(f"Output = {ltOdd}")