userin=int(input("Enter the 3-digit number "))

n1= userin%10
n2= userin//10%10
n3= userin//100

if (n1+n2+n3)%2==0 :
    print("Sum of all digits is an even number.")
else :
    print("Sum of all digits is an odd number.")

