str1 = "Avenger 4 END GAME was released in Year 2019"

def sumOfDigitsFromString(strInput):

 sum_digit = 0

 for i in strInput:
    if i.isdigit():
        sum_digit += int(i)
        
 print(sum_digit)
 
sumOfDigitsFromString(str1)