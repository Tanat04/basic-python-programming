def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    output = ''
    for i in digits[::-1]:
        output+=str(i)
    return output
n = int(input("Enter the number to want to convert: "))
b = int(input("Enter the base you want to convert till to: "))
result = numberToBase(n,b)
print('**Question 2**')
for i in range(2,b+1):
    value = numberToBase(n,i)
    print(f"The base {i} of the base 10, {n} is {value}.")
print()
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")