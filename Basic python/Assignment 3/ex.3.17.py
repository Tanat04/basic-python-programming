shopping=int(input("Enter shopping: "))
hour=int(input("Enter hours: "))
minute=int(input("Enter minutes: "))

hour=hour*60
time=hour+minute
fraction=time//30

#if fraction == float: 
#    fraction += 1

if minute > 0 and minute <= 30 :
    fraction += 0
    print("Its less than 30 min")
elif minute > 30 and minute <= 60 :
    fraction +=1
    print("Its more than 30 min")
    
if shopping >= 500 and fraction > 4 :
    print(f"""The parking fee for the first 2 hours is free.\nYou have to pay {(fraction-4)*30} baht for the parking fee.""")      
elif shopping >= 500 and fraction <= 4 :
    print("The parking fee for the first 2 hours is free.")

if shopping < 500 and fraction > 2 :
    print(f"""The parking fee for the first 1 hours is free.\nYou have to pay {(fraction-2)*30} baht for the parking fee.""")
elif shopping < 500 and fraction <= 2 :
    print("The parking fee for the first 1 hours is free.")

if shopping >=2000:
    print("The parking fee is 120 bath")
    
        
    
   
        
        
    
