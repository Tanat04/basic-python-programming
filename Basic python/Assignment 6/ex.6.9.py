sen = "You are my sunshine, you are my everything."
old="are"
new="were"

while True:
    index=sen.find(old)
    if index==-1:
        break
    sen=f"{sen[0:index]}{new}{sen[index+len(old):len(sen)]} "
print(sen)