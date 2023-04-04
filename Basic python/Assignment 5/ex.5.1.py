num=int(input("Till what Table do you want?: "))

print("\t x*1\t x*2\t x*3\t x*4\t x*5\t x*6\t x*7\t x*8\t x*9\t x*10\t x*11\t x*12")

count= 1
while count<=num:
    print(f"x = {count}",end="")
    x= 1
    while x<=12:
        print("\t","%3d"%(x*count),end="")
        x+= 1
    count+= 1
    print()
