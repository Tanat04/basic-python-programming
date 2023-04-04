sen=input("Enter string: ")
upper=0
lower=0
space=0
digit=0
str=""
if sen.isdigit():
    print(sen)
else:
    for i in sen:
        if i.isupper():
            str+=i.lower()
            upper+=1
        if i.islower():
            str+=i.upper()
            lower+=1
        elif ord(i)==32:
            str+=i
            space+=1
        elif i.isdigit():
            str+=i
            digit+=1

    print(upper,"Uppercase")
    print(lower,"Lowercase")
    print(space,"Spaces")
    print(digit,"digit")
    print(str)