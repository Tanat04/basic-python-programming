height=int(input("Enter your height "))

if height<80 :
    print(f"Your height is {height} and you are too small for this ride.")
elif height>=80 and height<180 :
    print(f"You are ok for this ride.")
else :
    print(f"Your height is {height}, its too tall for this ride")
