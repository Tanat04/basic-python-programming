firstInt = int(input("Enter the first integer: "))
secondInt = int(input("Enter the second integer: "))

if firstInt < secondInt :
    print(f"Output: " , end = "")
    count = firstInt
    while count <= secondInt:
        if count == secondInt:
            print(f"{count}" , end = "")
        else:
            print(f"{count}" , end = ",")
        count += 1
else:
     print(f"Output: " , end = "")
     count= firstInt
     while count >= secondInt:
         if count == secondInt:
            print(f"{count}" , end = "")
         else:
            print(f"{count}" , end = ",")
         count -= 1
         
