sentence= "Enter a positive integer(to terminate enter a negative number:"

userin= 0
total = 0
sm = 0

while userin >= 0:
    userin = int(input(sentence))
    if userin >= 0:
        total += 1
        sm += userin

print(f"The total of positive number entered is {total}")
print(f"The sum of all positive integer(s)is {sm}")