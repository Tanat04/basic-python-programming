sentence=input("Enter sentence here: ")

for i in sentence:
    if i.isdigit():
        sentence=sentence.replace(i," ")
print(sentence)