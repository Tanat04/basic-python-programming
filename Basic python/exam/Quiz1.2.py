kg=float(input("Enter your weight in kilograms: "))
meters=float(input("Enter your height in meters: "))

if meters == 0:
    print("Height cannot be Zero. Please try again.")
else:
    result=kg/meters**2
    if result<18.5:
        print(f"Your BMI is {'%.2f'%(result)},you are underweight.")
    elif result >= 18.5 and result<25:
        print(f"Your BMI is {'%.2f'%(result)},you are normal.")
    elif result >= 25 and result<30:
        print(f"Your BMI is {'%.2f'%(result)},you are overweight.")
    elif result >=30:
        print(f"Your BMI is {'%.2f'%(result)},you are obese.")
