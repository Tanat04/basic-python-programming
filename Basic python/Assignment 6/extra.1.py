lt=[0,1,2,3,4,5,6,7,8,9,10,11]

tanat=2
dev=4

x=int(input("How many step you want Tanat to move? " ))
y=int(input("How many step you want Dev to move? " ))

for i in range(x):
    tanat-=1
for j in range(y):
    dev+=1

if lt[tanat]==lt[dev]:
    print(f"Tanat and dev are at the same house,house {lt[tanat]}")
else:
    print(f"Tanat is at house {lt[tanat]} and dev is at house {lt[dev]}.")
