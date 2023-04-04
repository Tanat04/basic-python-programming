n=int(input("n: "))

line=0

while line<n:
    space = n-line-1
    while space>0:
        print(end=" ")
        space-=1
    star=line+1
    while star>0:
        print("*",end=" ")
        star-=1
    line+=1
    print()

linex=0
while linex<n:
    spacex=linex+1
    while spacex>0:
        print(end=" ")
        spacex-=1
    linex+=1
    star=n-linex
    while star>0:
        print("*",end=" ")
        star-=1
    print()
    
    
    
    
