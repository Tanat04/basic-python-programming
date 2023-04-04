def isOdd(n):
    if n% 2 ==1:
        return True
    else:
        return False

num= int(input("Enter number: "))
if isOdd(num):
    print("Its an odd number.")
else:
    print("Its an even number.")