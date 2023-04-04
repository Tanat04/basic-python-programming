print("***Donut sales program***")
amount=int(input("How many donuts do you want to buy : "))
number=0
totalsales=0
while amount>=0:
    number+=amount
    price=35
    cost=price*amount
    if amount > 50:
        discount=cost-(0.2*cost)
        print(f"The cost is {'{:.2f}'.format(discount)} baht.")
        totalsales+=discount
    elif amount>=20:
        discount=cost-(0.1*cost)
        print(f"The cost is {'{:.2f}'.format(discount)} baht.")
        totalsales+=discount
    elif amount>=0:
        print(f"The cost is {'{:.2f}'.format(cost)} baht.")
        totalsales+=cost
    amount=int(input("How many donuts do you want to buy : "))

print()
print(f"Total donut sales today was {number} donuts equaling {'{:.2f}'.format(totalsales)} baht.")
