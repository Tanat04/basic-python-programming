print("Assume that your date of birth is 1 January.")
yr=int(input("Enter your year of birth (A.D.): "))

todayYr=2021
age=todayYr-yr

for i in range(age,0,-1):
    print(f"By December {todayYr}, you are {i} years old.")
    todayYr-= 1
