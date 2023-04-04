# Id: 6410381
# Name: Tanat Arora

#Importing Logics
from AcademicModule import *

StartProgram() 

decide = -1

#doing a while loop to continously ask user to intereact with a program.
while decide != 0:
    if decide == 1:
        AddNewAcademicRecords()
    elif decide == 2:
        RemoveAcademicRecords()
    elif decide == 3:
        displayRecordsBySem()
    elif decide == 4:
        AcademicResultsByGrade()
    elif decide == 5:
        NumberOfCoursesWithGrades()
    elif decide == 6:
        UpdateAcademicModule()
    elif decide == 7:
        CalculateGPA()
    elif decide == 8:
        StartProgram()
    else:
        print("Error: Please enter number from 1-7, 8 to review choices again, 0 to exit.")
        print()
    decide=int(input("Enter option (1-7, 8 to review choices again, 0 to exit): "))
print()
print("Goodbye!! See you again.")