input=int(input("Enter 3 digit number"))
 
if input//100 %2==0 :
    print("I am sure either 2, 4, 6, or 8 must be a left-most digit.")
else :
    print("I know that the number you entered starts with either 1, 3, 5, 7, or 9.")
