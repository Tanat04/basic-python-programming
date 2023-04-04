rate=float(input("Conversion rate(BTH/USD): "))
decide=int(input("Enter 1 for US Dollar to Thai Bath, enter 2 otherwise: "))
if decide==1:
    us=float(input("US dollar: "))
    print()
    print(f"{us}$ = {'{:.3f}'.format(us*rate)}B.")
elif decide==2:
    bath=float(input("Thai Baht: "))
    print()
    print(f"{bath}B = {'{:.3f}'.format(bath/rate)}$.")
else:
    print("Error!!You can only type '1' or '2'.")