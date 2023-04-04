sentence=input("Enter sentence here: ")
for i in sentence:
    if 48<=ord(i)<=57:
        print(" ",end="")
    elif 65<=ord(i)<=90:
        print("*",end="")
    else:
        print(i,end="")

