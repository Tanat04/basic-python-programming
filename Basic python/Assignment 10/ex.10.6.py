def easydecrypt(en_strs,shift):
    new=""
    for l in en_strs:
        new+=chr(ord(l))
    return new

def easyencrypt(en_strs,shift):
    new=""
    for l in en_strs:
        new+=chr(ord(l) + shift)
    return new

letter=input("Enter the message you want to decrypt: ")
shift=int(input("Enter the number you want to shift: "))
print()
encrypt=easyencrypt(letter,shift)
print("The encrypt messages is: ", encrypt)
decrypt=easydecrypt(letter,shift)
print("The decrypt messages is: ", decrypt)