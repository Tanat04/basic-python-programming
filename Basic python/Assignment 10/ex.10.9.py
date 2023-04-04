decide=input("For encrypt write encrypt, for decrypt write decrypt: ")

if decide =="encrypt":
    def easyencrypt(en_strs,shift,direction):
        lower_base=ord("a")
        upper_base=ord("A")
        new=""
        for l in en_strs:
            if direction == "l":
                if ord(l) == 32:
                    new+= " "
                elif 65<= ord(l) <= 90:
                    new+=chr(((ord(l)-upper_base - shift)%26)+upper_base)
                elif 97<= ord(l) <= 122:
                    new+=chr(((ord(l)-lower_base - shift)%26)+lower_base)
            elif direction == "r":
                if ord(l) == 32:
                    new+= " "
                elif 65<= ord(l) <= 90:
                    new+=chr(((ord(l)-upper_base + shift)%26)+upper_base)
                elif 97<= ord(l) <= 122:
                    new+=chr(((ord(l)-lower_base + shift)%26)+lower_base)
            else:
                print("Error! You can only type 'l' or 'r'.")
                break
        return new

    letter=input("Enter the message you want to encrypt: ")
    shift=int(input("Enter the number you want to shift: "))
    direction=input("Which direction do you want to encrypt your word.: ")

    encrypt=easyencrypt(letter,shift,direction)
    print("The encrypt messages is:",encrypt)
elif decide =="decrypt":
    def easydecrypt(en_strs,shift,direction):
        lower_base=ord("a")
        upper_base=ord("A")
        new=""
        for l in en_strs:
            if direction == "l":
                if ord(l) == 32:
                    new+= " "
                elif 65<= ord(l) <= 90:
                    new+=chr(((ord(l)-upper_base - shift)%26)+upper_base)
                elif 97<= ord(l) <= 122:
                    new+=chr(((ord(l)-lower_base - shift)%26)+lower_base)
            elif direction == "r":
                if ord(l) == 32:
                    new+= " "
                elif 65<= ord(l) <= 90:
                    new+=chr(((ord(l)-upper_base + shift)%26)+upper_base)
                elif 97<= ord(l) <= 122:
                    new+=chr(((ord(l)-lower_base + shift)%26)+lower_base)
            else:
                print("Error! You can only type 'l' or 'r'.")
                break
        return new
    
    letter=input("Enter the message you want to decrypt: ")
    shift=int(input("Enter the number you want to shift: "))
    direction=input("Which direction do you want to decrypt your word.: ")

    decrypt=easydecrypt(letter,shift,direction)
    print("The decrypt messages is:",decrypt)
else:
    print("Error! You can only type 'encrypt' or 'decrypt'.")

