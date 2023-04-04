sen=input("Enter a message: ")

for i in sen.upper():
    i=ord(i)
    if i==32:
        print(" ",end="")
    else:
        result=chr(((i-65+3)%26)+65)
        print(result,end="")
