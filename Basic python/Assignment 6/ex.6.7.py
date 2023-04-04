sen=input("Write a sentence: ")
n=(len(sen))

if n%2==0:
    firstHaft=n//2
    print("First haft: ",end="")
    for i in range(firstHaft):
        print(sen[i],end="")
    print()
    print("Second haft: ",end="")
    for i in range(firstHaft,n):
        print(sen[i],end="")
else:
    firstHaft=(n+1)//2
    print("First haft: ",end="")
    for i in range(firstHaft):
        print(sen[i],end="")
    print()
    print("Second haft: ",end="")
    for i in range(firstHaft,n):
        print(sen[i],end="")