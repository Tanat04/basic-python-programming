def ConvertBinary(binary):
    binary = list(str(binary))
    binary = binary[::-1]
    sm = 0
    power = 0

    for i in binary:
        if i == "1":
            sm = sm + 2**power
        power += 1
    return sm

binary=int(input("Enter binary number: "))
outcome=ConvertBinary(binary)
print("The number is ",outcome)