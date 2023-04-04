n=int(input("Enter n: "))
sm = 0
count=1

if n <= 0:
    print("The entered value must be greater than ZERO!")
else:
    while count <= n:
        if count < n :
            print(f"{count}+" , end = "")
        elif count == n:
            print(f"{count}" , end = "")
        sm += count
        count += 1
    print(f"={sm}")
