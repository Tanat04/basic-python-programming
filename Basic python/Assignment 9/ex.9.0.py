def FindSumOddWithCondition(inputList):
    sm=0
    count=0
    for i in inputList:
        if i% 2==1:
            if 5<i<20:
                sm+=i
                count+=1
    return sm,count

x=[1,7,13,18,15]
totalSum,totalNo=FindSumOddWithCondition(x)
print(totalSum)
print(totalNo)
print(FindSumOddWithCondition(x))