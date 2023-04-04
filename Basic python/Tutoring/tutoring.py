# # String => {"Hello", "AbCd"}
# # Integers => {-9, -23, 0, 12, 34}
# # Float => {2.3, 0.33, -0.4}
# # List => "Have to use square bracket" [12, 2.43, "Hello"]

# # Normal printing:
# print("My name is john")

# # f-string printing:
# name = "john"
# print(f"My name is {name}")

# age = 12
# print(f"My name is {name}. I am {age} years old.")

# #Limiting floats
# pi_value = 22/7
# new_Pi_value = round(pi_value, 2)
# print(f"Pi value: {pi_value}")
# print(f"Two decimal place Pi value: {new_Pi_value}")

# # While loop
# x = 0
# # while x < 10:
# #     print(x)

# while x < 10:
#     print(x)
#     x = x + 1

# while x <= 10:
#     print(x)
#     x = x + 1

#For loop
#for 'variable' in range('start','end','step')
# for x in range(1, 10):
#     print(x)

# for x in range(1, 11):
#     print(x)

# for x in range(0, 21, 2):
#     print(x)

# for x in range(21, 0, -2):
#     print(x)

# # Function
# def welcome():
#     print("Hello world")

# welcome()
# welcome()

# def multiply(x, y):
#     return x * y

# multiply(2,4)
# print(multiply(4,4))

# #If & Else
# a = 10
# if a == 10:
#     print("Yes")
# else:
#     print("No")

# if a % 1 == 0:
#     print("1")
# elif a % 2 == 0:
#     print("2")

# # Moderation
# a = 10 % 3
# b = 10 % 4
# c = 4 % 10
# print(a)
# print(b)
# print(c)

# #Division
# a = 10 / 3
# b = 10 // 3
# print(a)
# print(b)

# #Convert
# number = "123"
# print(number)
# print(type(number))

# number = int(number)
# print(number)
# print(type(number))

# number = float(number)
# print(number)
# print(type(number))

# # text = "Hello World!"
# # print(type(int(text)))

# # ASCII
# letter = "a"
# print(ord(letter))

# number = 97
# print(chr(number))

# a = "1,2,3,4,5,6,7"
# b = "1 2 3 4 5 6 7"
# c = "1/2/3/4/5/6/7"
# # d = "1.2.3.4.5.6.7"

# print(a.split(","))
# print(b.split(" "))
# print(c.split("/"))
# # print(d.split("."))

# #List
# a = [1,2,3]
# print(a)

# a.append(4)
# print(a)

# a.remove(3)
# print(a)

# a[0] = 999
# print(a)

# # SLice List& Index
# a = [1,2,3,4,5,6]

# print(a)
# print("Index 0 : ", a[0])
# print("Index 1 : ", a[1])

# print(a[0:2])
# print(a[0:])
# print(a[0:-1])

# # Sort
# a = [5,2,3,1,4]
# a.sort()
# print(a)

# b = [5,2,3,1,4]
# print(sorted(b))

# # Lenght of the list
# a = [1,2,3,4,5]
# print(len(a))

# # Upper & Lower
# a = "hEllOWorld"
# print(a.upper())
# print(a.lower())

# #String format
# print("My name" + " is" + " Doraemon")
# a = "My name"
# b = "is"

# print(a + b + " Doraemon")

# # Abstract
# a = 5-10
# print(a)
# print(abs(a))

# print(abs(3))