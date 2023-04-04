def mid(x,y,z):
    if x > y and x< z:
        print(f"Mid number is {x}.")
    elif x < y and x> z:
        print(f"Mid number is {x}.")
    elif y> x and y< z:
        print(f"Mid number is {y}.")
    elif y< x and y> z:
        print(f"Mid number is {y}.")
    elif z > x and z < y:
        print(f"Mid number is {z}.")
    elif z < x and z > y:
        print(f"Mid number is {z}.")
    if x==y and x==z:
        print("Every value are the same.")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
mid(x,y,z)