from ex11_8_1 import *

# Testing splitType function
intLt , floatLt = SplitType([2,2.2,3,3.3,4,4.4,5,5.5])
print(f"Int list are: {intLt} and Float list are: {floatLt}")

#Testing ListofOdd function
result = listofOdds([1,2,3,4,5,6,7,8,9])
print(f"The list of odds are: {result}")

#Testing KeepTwoDup function
numlist=[1,2,2,2,3,4,5,5,5,1,2,3,3]
outlist=KeepTwoDuplicate(numlist)
print(f"outlist = {outlist}")