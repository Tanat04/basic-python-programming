numX=input("Enter first number: ")
numY=input("Enter second number: ")
numZ=input("Enter third number: ")

if numX > numY and numY > numZ :
    print(f"The mid value is {numY}")
elif numZ > numY and numY > numX :
      print(f"The mid value is {numY}")
elif numY > numX and numX > numZ :
      print(f"The mid value is {numX}")
elif numZ > numX and numX > numY :
      print(f"The mid value is {numX}")
elif numY > numZ and numZ > numX :
      print(f"The mid value is {numZ}")
elif numX > numZ and numZ > numY :
      print(f"The mid value is {numZ}")

