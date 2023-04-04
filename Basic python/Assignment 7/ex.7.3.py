letter=input("Input: ").split(" ")
n=int(input("Enter a value for n: "))
print("Output: ",end="")

for i in letter:
    for j in range(1,n+1):
        print(i.upper()+str(j) ,end=" ")
        