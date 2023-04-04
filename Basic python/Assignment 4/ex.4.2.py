total = int(input("How many numbers? " ))
sm = 0
num = 1

while num <= total:
    number = float(input(f"Number#{num}: "))
    sm += number
    num += 1

result = sm / total

print(f"The average of these number is {result}")
    
