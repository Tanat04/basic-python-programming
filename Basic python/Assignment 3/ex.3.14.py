x1=int(input("Enter x1 "))
x2=int(input("Enter x2 "))
x3=int(input("Enter x3 "))

if x2 % x3 == 0 and x1 % x3 == 0:
    print("x3 is a factor of both x1 and x2.")
elif x2 % x3 != 0 and x1 % x3 == 0 :
    print("x3 is the factor of x1.")
elif x2 % x3 == 0 and x1 % x3 != 0 :
    print("x3 is the factor of x2.")
elif x2 % x3 != 0 and x1 % x3 != 0 :
    print("x3 is neither a factor of x1 nor x2.")
    
#THE STEP BELOW CAN ALSO BE USE AS THE LAST STEP ABOVE...
#else:
#    print("x3 is neither a factor of x1 nor x2.")
    
