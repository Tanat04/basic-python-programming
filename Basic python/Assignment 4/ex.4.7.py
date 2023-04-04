num=int(input("Input number: "))
sm = 0
num2 = num

while num2 > 0:
    digit=num2%10
    sm += digit
    num2=num2 // 10
print(f"The sum of each digit in {num} is {sm}.")

