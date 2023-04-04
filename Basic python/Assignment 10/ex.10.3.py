def combination(n,r):
    return(fact(n)/(fact(r)*fact(n-r)))
def fact(n):
    shift = 1
    for i in range(2,n-1):
        shift=shift*i
    return shift
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
print(int(combination(n,r)))