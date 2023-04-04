numA=int(input("Enter numA: "))
numB=int(input("Enter numB: "))

highValue=0
lowValue=0
sm= 0

if numA < numB:
    lowValue+=numA
    highValue+=numB
else:
    lowValue+=numB
    highValue+=numA

for i in range(lowValue,highValue+1):
    if i% 3 ==0 and i% 7 ==0:
        print("",end="")
    else:
        print(i,end=" ")
        sm+= i
    if sm > highValue*5:
            break
        
