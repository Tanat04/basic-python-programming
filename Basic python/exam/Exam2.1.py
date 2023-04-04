def recurrenceRelation(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 3 * recurrenceRelation(n-1) + recurrenceRelation(n-2) + 4

num= int(input("Enter a positive integer: "))
print()
if num <= 0:
    print("Please enter a positive integer!")
else:
    for i in range(1,num+1):
        print(f"n = {i},f({i}) = {recurrenceRelation(i)}")