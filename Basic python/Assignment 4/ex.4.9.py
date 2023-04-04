num=int(input("Input number: "))

print(f"Output number: ",end="")

while num > 0:
    digit=num %10
    print(digit,end="")
    num= num//10

