L1 = [100, 10, 200, 25, 7, 20]
L2 = [3, -54, 232, 4, 76, 340]

L1.sort()
L2.sort()
print(L1)
print(L2)

i= j= 0
sm=[]

if len(L1) == len(L2):
   while i < len(L1) and j< len(L2):
      if L1[i] < L2[j]:
         num = L2[j]-L1[i]
         sm.append(num)
      else:
         num = L1[i]- L2[j]
         sm.append(num)
      i+=1
      j+=1
   print(sm)
   print(min(sm))      
else:
   print("Error!!! the amount of number put should be equal to each other.")