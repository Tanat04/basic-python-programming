def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def avgList(numlist):
    return sum(numlist)/len(numlist)

def sumofoddpos(numlist):
    newLt=[]
    for num in range(len(numlist)):
        if num%2 == 0:
            newLt.append(numlist[num])
        else:
            continue
    return sum(newLt)

