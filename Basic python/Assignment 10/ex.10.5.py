def easyencrypt(letter,shift):
    new=""
    for l in letter:
        new+=chr(ord(l) + shift)
    return new

letter=input("Enter the message you want to decrypt: ")
shift=int(input("Enter the number you want to shift: "))

n=easyencrypt(letter,shift)
print("The decrypt messages is: ", n)