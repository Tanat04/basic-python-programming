cardNo = list(input("Enter 16-digit credit card  card number: ").strip())
check = cardNo.pop()
cardNo.reverse()
lt= []
for index, digit in enumerate(cardNo):
    if index % 2 == 0:
        twoD = int(digit) * 2
        if twoD > 9:
            twoD = twoD - 9
        lt.append(twoD)
    else:
        lt.append(int(digit))

total = int(check) + sum(lt)

if total % 10 == 0:
    print("This is a valid card number.")
else:
    print("This is an invalid card number.")