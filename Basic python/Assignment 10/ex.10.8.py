decide=input("For encrypt write encrypt, for decrypt write decrypt: ")

if decide =="encrypt":
    def easyencrypt(en_strs,shift,direction):
        base=ord("a")
        new=""
        for l in en_strs:
            if direction == "l":
                if ord(l) == 32:
                    new+= " "
                else:
                    new+=chr(((ord(l)-base - shift)%26)+base)
            elif direction == "r":
                if ord(l) == 32:
                    new+= " "
                else:
                    new+=chr(((ord(l)-base + shift)%26)+base)
            else:
                print("Error! You can only type 'l' or 'r'.")
                break
        return new

    letter=input("Enter the message you want to encrypt: ").lower()
    shift=int(input("Enter the number you want to shift: "))
    direction=input("Which direction do you want to encrypt your word.: ")

    encrypt=easyencrypt(letter,shift,direction)
    print("The encrypt messages is:",encrypt)
elif decide =="decrypt":
    def easydecrypt(en_strs,shift,direction):
        base=ord("a")
        new=""
        for l in en_strs:
            if direction == "l":
                if ord(l) == 32:
                    new+= " "
                else:
                    new+=chr(((ord(l)-base - shift)%26)+base)
            elif direction == "r":
                if ord(l) == 32:
                    new+= " "
                else:
                    new+=chr(((ord(l)-base + shift)%26)+base)
            else:
                print("Error! You can only type 'l' or 'r'.")
                break
        return new
    
    letter=input("Enter the message you want to decrypt: ").lower()
    shift=int(input("Enter the number you want to shift: "))
    direction=input("Which direction do you want to decrypt your word.: ")

    decrypt=easydecrypt(letter,shift,direction)
    print("The decrypt messages is:",decrypt)
else:
    print("Error! You can only type 'encrypt' or 'decrypt'.")

