def separateChar(myStr):

    str1 = ''
    upper_char = ''
    lower_char = ''
    digit_char = ''

    for l in myStr:
        if l.isupper():
            upper_char+= l
        elif l.islower():
            lower_char+= l
        elif l.isdigit():
            digit_char+= l
        else:
            str1+=l

    print(upper_char)
    print(lower_char)
    print(digit_char)

print("**Question 4**")
str1 = "Avenger 4 END GAME was released in Year 2019"
separateChar(str1)

print("= = = = = = = =")

str2 = "I am 109 years old"
separateChar(str2)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")