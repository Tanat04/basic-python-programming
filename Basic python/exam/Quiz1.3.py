num=int(input("Enter number: "))

sm =0
if num<3:
    print("No results")
else:
    for i in range(1,num+1):
        if i%3 == 0 or i%5==0 or i%6==0:
            if  i == num-2 or i == num-1:
                print(i,end="")
                sm+=i
            else:
                print(i,end=",")
                sm+=i
    print()
    print(sm)
