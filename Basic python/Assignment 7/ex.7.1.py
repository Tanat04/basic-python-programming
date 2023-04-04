word=input("Enter words: ")
word=word.split(" ")
count=0

for w in word:
    if len(w)>=4:
        if w[0]==w[-1]and w[1]==w[-2]:
            count+=1
print("Number of words that meets the requirements is :",count)
