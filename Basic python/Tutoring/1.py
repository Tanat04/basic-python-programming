speed = int(input("Whats the speed: "))

if speed < 70:
    print("Ok")
else:
    exceed = speed - 70
    value = exceed//5
    print(type(value))
    if type(value) == int:
        value = value - 0.1
        print(value)
    else:
        print(((value//1)+1)*100)

