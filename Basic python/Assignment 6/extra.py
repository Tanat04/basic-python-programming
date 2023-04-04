sec=int(input("Enter second: "))
if sec <=0:
    print("")
else:
    print(f"{sec} seconds-> ",end="")
    min = sec//60
    sec=sec%60
    hr=min//60
    min=min%60

    if hr!=0:
        print(f"{hr} hours",end=" ")
    if min!=0:
        print(f"{min} minutes",end=" ")
    if sec!=0:
        print(f"{sec} seconds",end=" ")
