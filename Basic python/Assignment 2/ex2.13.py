sqMeter=float(input("Enter an area size in square-meter: "))

sqInch= sqMeter* 1550
sqFeet= sqMeter* 10.764
sqKm= sqMeter/1e+6

print(f"The area size in square-inch is {sqInch}")
print(f"The area size in square-feet is {sqFeet}")
print(f"The area size in square-km is {sqKm}")
