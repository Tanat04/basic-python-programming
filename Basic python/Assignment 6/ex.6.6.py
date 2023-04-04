sen=input("Enter string: ")

TotalAlp=0
upper=0
lower=0
numeric=0
other=0

for i in sen:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        TotalAlp+=1
    if 65<=ord(i)<=90:
        upper+=1
    if 97<=ord(i)<=122:
        lower+=1
    elif 48<=ord(i)<=57:
        numeric+=1
    elif ord(i)>90 or ord(i)<65:
        other+=1
print("Total alphabet = ",TotalAlp)
print(f"Uppercase = {upper}")
print(f"Lowercase = {lower}")
print("Numeric = ",numeric)
print("Other letters(including space) = ",other)
