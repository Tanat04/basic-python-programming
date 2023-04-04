# Id: 6410381
# Name: Tanat Arora

# Importing read,write functions
from ReadWriteModule import *

# Print instruction about 'How to run a program and what can a program do.'
def StartProgram():
    print("""AcaRec Version 1.0
PERSONAL ACADEMIC RECORDS
---- ---- ---- ---- ---- ---- ----
1. Add new academic record
2. Remove a specific academic record
3. Display academic records by semester
4. Display academic records by grade result
5. Display the number of courses for each grade results
6. Update a grade result to a specific academic record
7. Calculate the overall G.P.A. and total credits
8. To review choices again 
0. Exit the program
---- ---- ---- ---- ---- ---- ----
""")

# Add new academicrecords to a csv file
def AddNewAcademicRecords():
    print("---- ---- ---- ---- ---- ---- ----")
    AcaYear = input("Enter academic year: ")
    AcaTerm = input("Enter academic term: ")
    CourseCode = input("Enter course code: ")

    Data = readFile('academicrecords')
    DataToCheck = AcaYear + AcaTerm + CourseCode

    # Checking if the data are already in the file.
    for line in Data:
        if line[0] + line[1] + line[2] == DataToCheck:
            print(f"Error: {CourseCode} already exist in {AcaTerm}/{AcaYear}!")
            return

    # If the data is not repeated then continue.
    SecNo = input("Enter section number: ")
    grade = input("Enter grade results: ")
    CourseCredit = input("Enter course credit: ")

    # Creating a new list that contains original student as 'Data' and append a new record taken by user as newRecords.
    newData = Data
    newRecords = [AcaYear, AcaTerm, CourseCode, SecNo, grade, CourseCredit]
    newData.append(newRecords)

    #Write a original records with sorted new data added.
    newData = sorted(newData)
    write('academicrecords',newData)  
    print(f"{CourseCode} added.")
    print()

# remove specific record by coursecode
def RemoveAcademicRecords():
    print("---- ---- ---- ---- ---- ---- ----")
    CourseCode = input("Enter course code: ")
    Data = readFile('academicrecords')

    # create a new list to append the course code that is npt same as the one user input
    newData = []
    count = 0

    # check if the coursecode taken from user is there in our data or not
    for row in Data:
        if row[2] != CourseCode:
            newData.append(row)
        else:
            count += 1
            continue

    # if there is no data we will not continue.
    if count == 0:
        print(f"Error: There is no academic to remove for {CourseCode}.")
        print()
        return
    
    # write a new data with a list create excluding the row with the same coursecode user input.
    write('academicrecords', newData)
    print(f"{CourseCode} removed.")
    print()

# Display academic records by semester
def displayRecordsBySem():
    print("---- ---- ---- ---- ---- ---- ----")
    Data = readFile('academicrecords')

#Checking if the data is empty or not
    if len(Data) == 0:
        print("Error: No academic records found!")
    else:
        newFile = {}
        for row in Data:
            termyear = (row[1],row[0])
            if termyear not in newFile:
                newFile[termyear] = [[row[2],f"({row[3]})",row[4]]]
            else:
                newFile[termyear].append([row[2],f"({row[3]})",row[4]])
        for termyear in newFile.__reversed__():
            print(f"Semester {termyear[0]}/{termyear[1]}")
            for course in newFile.get(termyear):
                print ("{:<8} {:<10} {:<10}".format(course[0],course[1],course[2]))
            print()

# display academic records by grade taken by user input.
def AcademicResultsByGrade():
    print("---- ---- ---- ---- ---- ---- ----")
    Grade = input("Enter grade result to lookup: ")
    Data = readFile('academicrecords')
    count = 0
    
    # check if row has same grade as user input 
    for row in Data:
        if row[4] == Grade:
            count += 1
        else:
            continue
    
    # If there is no academic records with that grade then print as i wrote below.
    if count == 0:
        print(f"Error: No academic records found for {Grade} grade!")
        print()
        return

    # if yes then display that row's coursecode,section and grade.
    else:
        print("Coursecode\tSection\t\tGrade")
        for row in Data:
            if row[4] == Grade:
                print(row[2] +'\t\t  '+ row[3] + '\t\t' + row[4])
    print()

# display number of courses with grade.
def NumberOfCoursesWithGrades():
    print("---- ---- ---- ---- ---- ---- ----")
    Data = readFile('academicrecords')

    # teaching a program to know what are grade A,B,C,D,F etc 
    def CalculateNumbersOfGrades():

        # creating a variable for each grade that we have
        gA = 0
        gAMinus = 0
        gB = 0
        gBPlus = 0
        gBMinus = 0
        gC = 0
        gCPlus = 0
        gCMinus = 0
        gD = 0
        gF = 0
        gS = 0

        # counting numbers of each grade
        for line in Data:
            if line[4] == 'A':
                gA += 1
            elif line[4] == 'A-':
                gAMinus += 1
            elif line[4] == 'B':
                gB += 1
            elif line[4] == 'B+':
                gBPlus += 1
            elif line[4] == 'B-':
                gBMinus += 1
            elif line[4] == 'C':
                gC += 1
            elif line[4] == 'C+':
                gCPlus += 1
            elif line[4] == 'C-':
                gCMinus += 1
            elif line[4] == 'D':
                gD += 1
            elif line[4] == 'F':
                gF += 1
            elif line[4] == 'S':
                gS += 1
        #printing a number of each grade that is not zero
        if gA != 0:
            print(f"Grade A       {gA} course(s)")
        if gAMinus != 0:
            print(f"Grade A-      {gAMinus} course(s)")
        if gB != 0:
            print(f"Grade B       {gB} course(s)")
        if gBPlus != 0:
            print(f"Grade B+      {gBPlus} course(s)")
        if gBMinus != 0:
            print(f"Grade B-      {gBMinus} course(s)")
        if gC != 0:
            print(f"Grade C       {gC} course(s)")
        if gCPlus != 0:
            print(f"Grade C+      {gCPlus} course(s)")
        if gCMinus != 0:
            print(f"Grade C-      {gCMinus} course(s)")
        if gD != 0:
            print(f"Grade D       {gD} course(s)")
        if gF != 0:
            print(f"Grade F       {gF} course(s)")
        if gS != 0:
            print(f"Grade S       {gS} course(s)")
    # Calling a function that i create above
    CalculateNumbersOfGrades()
    print()

# Update specific grade record determine by coursecode,term,year.
def UpdateAcademicModule():
    print("---- ---- ---- ---- ---- ---- ----")
    AcaYear = input("Enter academic year: ")
    AcaTerm = input("Enter academic term: ")
    CourseCode = input("Enter course code: ")
    Data = readFile('academicrecords')
    DataToCheck = AcaYear + AcaTerm + CourseCode
    count = 0

    # creating a new list to append a original data with updated grade.
    newData=[]

    # Checking which row to change the grade
    for row in Data:
        if row[0] + row[1] + row[2] == DataToCheck:
            
            #If found row then ask user for new grade and append it to a new list
            grade = input("Enter grade result: ")
            newData.append([row[0], row[1], row[2], row[3], grade, row[5]])

            print(f"Updated grade result {AcaTerm}/{AcaYear} on {CourseCode} as {grade}")
            count += 1
        
        #if row is not the one user want to update then append it to new list.
        else:
            newData.append(row)

    # if no row found with the coursecode and other data user gave then print as below and return.
    if count == 0:
        print(f"Error: {CourseCode} not found for {AcaTerm}/{AcaYear}!")
        print()
        return
    
    # write a new list with updated grade
    write('academicrecords', newData)
    print()

# Calculate GPA and total credit
def CalculateGPA():
    print("---- ---- ---- ---- ---- ---- ----")
    Data = readFile("academicrecords")
    gpa = 0
    TotalCredit = 0

    #checking  if the file is empty or not.
    if Data == []:
        print("Error: No file found!")
        return

    # adding a credit from each row to a variable name 'TotalCredit'
    for row in Data:
        TotalCredit+=int(row[5])

    # Letting a program to know what are the value for each grades except the one with 'S' grade.
    for line in Data:
        grade= 0
        if line[5] != 0:
            if line[4] == 'A':
                grade = 4.00
            elif line[4] == 'A-':
                grade = 3.75
            elif line[4] == 'B+':
                grade = 3.25
            elif line[4] == 'B':
                grade = 3.00
            elif line[4] == 'B-':
                grade = 2.75
            elif line[4] == 'C+':
                grade = 2.25
            elif line[4] == 'C':
                grade = 2.00
            elif line[4] == 'C-':
                grade = 1.75
            elif line[4] == 'D':
                grade = 1.00
            elif line[4] == 'F':
                grade = 0
        else:
            continue

        # calculating GPA 
        gpa += (grade * int(line[5])) / TotalCredit

    #printing a result
    print(f"G.P.A. is {round(gpa , 2)}")
    print(f"Total Credit is {TotalCredit}")
    print()
