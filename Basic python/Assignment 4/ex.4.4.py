n=int(input("Enter n: "))

if n == 0 or n == 1:
    print(f"{n}! = 1 ")
elif n < 0:
    print("Error!!! The enter number should be more than Zero...")
else:
    print(f"{n}!=" ,end = "")
    fac = 1
    count = 1
    while count <= n:
        if count == n:
            print(f"{count}" , end = "")
        else:
            print(f"{count}x" , end = "")
        fac *= count
        count += 1
    print(f"= {fac}")
        
        
        

