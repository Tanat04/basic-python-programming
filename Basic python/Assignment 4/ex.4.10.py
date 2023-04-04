balance=float(input("Enter balance: "))
intRate=float(input("Enter interest rate: "))
years=int(input("enter years: "))

print(f"Enter initial account balance,interest rate and years respectively: {balance},{intRate},{years}.")
print("Year\tInt Rate\tInt Earned\tBalance")

annual = 1
while annual<=years:
    interest = balance*intRate/100
    balance+=interest
    print(f"{annual}\t{intRate}\t\t{'{:.2f}'.format(interest)}\t\t{'{:.2f}'.format(balance)}")
    intRate+=1
    annual+= 1
    
