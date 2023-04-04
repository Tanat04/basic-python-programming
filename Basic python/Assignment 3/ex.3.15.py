Fahrenheit=input("Enter Fahrenheit: ")
Fahrenheit=float(Fahrenheit)

Kelvin= ((Fahrenheit-32)*5/9) + 273.15
Celcius= (Fahrenheit-32)*5/9

if Kelvin >= 280 :
    print(f"The temperature is {Kelvin} Kelvin.")
elif Kelvin < 280 and Kelvin >= 265.3 :
    print("Too cold!!!!")
elif Kelvin < 265.3 :
    print("Too cold to live!!!")
    
print(f"The temperature is {Celcius} Celcius.")
