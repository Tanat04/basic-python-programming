def printHarry(n):
    if n == 1:
        return "Harry"
    else:
        return "Harry" + printHarry(n-1)
print(printHarry(3))