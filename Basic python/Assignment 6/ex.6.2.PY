sentence=input("Enter a sentence: ")
cha=input("Enter a character: ")
count=0

for i in sentence:
    if i == cha:
        count+=1
print(f"Total no. of character '{cha}' in this sentence = {count}")