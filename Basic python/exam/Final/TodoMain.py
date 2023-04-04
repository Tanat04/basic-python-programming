# TodoMain.py

from TodoLogic import *
 
startProgram()

option = '-1'

while option != '0':
    if option.isalpha(): 
        print("Error: You can only type in digits!")
        print()
    elif option == '1':
        CreateNew()
    elif option == '2':
        MarkStatusComplete()
    elif option == '3':
        showIncomplete()
    elif option == '4':
        showIncompleteByPriority()
    elif option == '5':
        summary()
    elif option == '6':
        removeTask()
    elif option == '7':
        markCompletes()
    else:
        print("Error: You can only type 0-7.")
    option = input("Enter option (1-7, 0 to exit): ")