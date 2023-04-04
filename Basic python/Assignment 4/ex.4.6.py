print("Enter 3 integer numbers, where as numX ≥ numY ≥ numZ.")

numX = int(input("numX: "))
numY = int(input("numY: "))
numZ = int(input("numZ: "))

num = numX
count = 0

while num <= numZ :
    if num % numY == 0 :
        count+=1
    num += 1
print(f"There are {count} numbers in {numX}...{numZ} that can be divisible by {numY}.")


