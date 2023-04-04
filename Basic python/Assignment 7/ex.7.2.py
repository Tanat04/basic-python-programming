word=input("Input: ").split(" ")
output=[]

for w in word:
    if w in output:
        continue
    else:
        output.append(w)
print("output: ",end="")
for i in output:
    print(i,end=" ")

