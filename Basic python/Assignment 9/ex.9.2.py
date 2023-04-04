def DoubleTriple(x):
    double=x**2
    triple=x**3
    return x,double,triple
num=int(input("Enter number here: "))
a,b,c=DoubleTriple(num)
print(f"{a}\n{b}\n{c}")
print(DoubleTriple(num))