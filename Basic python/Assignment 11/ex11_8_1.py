def SplitType(numlist):
    intLT=[]
    floatLt=[]
    for num in numlist:
        if isinstance(num, int):
            intLT.append(num)
        elif isinstance(num, float):
            floatLt.append(num)
        else:
            print(f"Type of {num} not idetified")
    return intLT , floatLt
#intLt , floatLt =SplitType([2,2.2,3,3.3,4,4.4])
#print(intLt,  floatLt)

def listofOdds(numlist):  
    if len(numlist) == 1:
        if numlist[0]% 2 == 0:
            return []
        else:
            return numlist
    else:
        if numlist[0]%2 == 0:
            return listofOdds(numlist[1:])
        else:
            return numlist[0:1] + listofOdds(numlist[1:])
#print(listofOdds([1,2,3,4,5]))

def KeepTwoDuplicate(numlist):
    seen={}
    lt=[]
    for num in numlist:
        if num not in seen:
            seen[num] = 1
            lt.append(num)
        else:
            if seen[num] == 1:
                seen[num] += 1
                lt.append(num)
    return lt
#rint(KeepTwoDuplicate([1,2,2,2,3,4,5,5,5,1,2,3,3]))
