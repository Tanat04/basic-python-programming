#n=int(input("Enter the numbers of element in the list: "))
lt=[4, 1, 2, 9, 7, 100, 5, 0, 99, 100]#for input u have to write "lt=list()"

#for i in range(n):
#    number=float(input("number: "))
#    lt.append(number)
#    print("",end="")
lt.sort()
n=len(lt)#You have to remove this line for the input method.

print("numbers =",lt) 
diff=99999999

for j in range(n-1):
    if lt[j+1]-lt[j]< diff:
        diff = lt[j+1]-lt[j]
print("The lowest different between two numbers is",diff)

