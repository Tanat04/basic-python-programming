print('''Welcome to CRUD Menu (students)
1. Create new student
2. List out students
3. Update the student name from Id
4. Delete the student from Id
5. List out students with batch (e.g. 62, 63, 64)
6. To review choices again
0. Terminate program''')
idList = [611000,621000,612000]
nameList = ["John", "Eddy","Tanat"]
choice = int(input("Enter the choice: "))
while choice != 0:
    if choice == 1:
        id = int(input("Enter the id: "))
        name = input("Enter the name: ")
        idList.append(id)
        nameList.append(name)
        print("Student added")
    elif choice == 2:
        for index in range(0, len(idList)):
            print(f"#{index+1} {idList[index]} {nameList[index]}")
    elif choice == 3:
        count = 0
        checkId= int(input("Enter the id of a student that you want to update: "))
        for index in range(0, len(idList)):
            if idList[index] == checkId:
                newName=input("Enter the new name of the student: ")
                nameList[index] = newName
                count +=1
        if count == 0:
            print("There is no student with the ID's you entered. Please try again.")
            print()
            choice = int(input("Enter the choice: "))
            continue
        print("Name's have been updated.")
    elif choice == 4:
        count = 0
        checkId = int(input("Enter the id of a student that you want to delete: "))
        for index in idList:
            if index == checkId:
                pos=idList.index(index)
                idList.remove(index)
                del nameList[pos]
                count+=1
        if count == 0:
            print("There is no student with the ID's you entered. Please try again.")
            print()
            choice = int(input("Enter the choice: "))
            continue
        print(f"Records of this student's ID:{checkId} have been deleted.")
    elif choice == 5:
        myDict={}
        seen=[]
        for num in idList:
            i=str(num)
            i=i[:2]
            if i not in myDict:
                myDict[i] = [num]
            else:
                myDict[i] += [num]
        print(myDict)
    elif choice == 6:
        print('''Welcome to CRUD Menu (students)
1. Create new student
2. List out students
3. Update the student name from Id
4. Delete the student from Id
5. List out students with batch (e.g. 62, 63, 64)
6. To review choices again
0. Terminate program''')
    else:
        print("Invalid choice!")
        print()
        choice = int(input("Enter the choice: "))
        continue 
    print()
    choice = int(input("Enter the choice: "))
print("Goodbye!")