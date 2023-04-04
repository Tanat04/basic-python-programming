# TodoLogic.py

from ToolBox import *

def startProgram():
    print("""TODO List Menu Driven
PERSONAL TASK REMINDER
---- ---- ---- ---- ---- ---- ----
1. Create a new task
2. Mark completes for a specific  task
3. Show incomplete tasks sort by priority
4. Show incomplete tasks for a specific priority
5. Show summary report
6. Remove a specific task
7. Mark completes for every tasks you have
""")

alltask = []

def CreateNew():
    print("---- ---- ---- ---- ---- ---- ----")
    name = input("Enter task name: ")
    prioLevel = input("Enter priority level: ")
    while not prioLevel.isdigit() or (int(prioLevel) < 1 or int(prioLevel) > 3):
        print("Error: Type 1-3")
        print()
        prioLevel = input("Enter priority level: ")
    prioName = priorityName(int(prioLevel))
    alltask.append([name,prioName,'I'])
    print(f"New task added at {getTime()}")    
    print()

def MarkStatusComplete():
    print("---- ---- ---- ---- ---- ---- ----")
    index = input("Enter task index: ")
    while int(index) > len(alltask):
        print("Error: Index not found. Please type again.")
        print()
        index = int(input("Enter task index: "))
    alltask[int(index)][2] = 'C'
    print(f"{alltask[int(index)][0]} completed at {getTime()}")
    print()

def showIncomplete():
    print("---- ---- ---- ---- ---- ---- ----")
    print("Priority\tTask(s)")
    seperate = []
    for task in alltask:
        if task[2] == 'I':
            seperate.append([task[0],task[1]])
    for i in seperate:
        if i[1] == 'High':
            print(f"High\t\t{i[0]}")
    for i in seperate:
        if i[1] == 'Medium':
            print(f"Medium\t\t{i[0]}")
    for i in seperate:
        if i[1] == 'Low':
            print(f"Low\t\t{i[0]}")
    print()

def showIncompleteByPriority():
    print("---- ---- ---- ---- ---- ---- ----")
    prioLevel = input("Enter priority level: ")
    while not prioLevel.isdigit() or (int(prioLevel) < 1 or int(prioLevel) > 3):
        print("Error: Type 1-3")
        print()
        prioLevel = input("Enter priority level: ")
    prioName = priorityName(int(prioLevel))
    print("Priority\tTask(s)")
    count = 0
    for task in alltask:
        if task[1] == prioName and task[2] == 'I':
            print(f"{prioName}\t\t{task[0]}")
            count += 1
    if count == 0:
        print("No tasks found under this priority!")
    print()

def summary():
    print("---- ---- ---- ---- ---- ---- ----")
    print("Summary Report")
    incomplete = []
    complete = []
    for task in alltask:
        if task[2] == 'I':
            incomplete.append(task[1])
        if task[2] == 'C':
            complete.append(task[1])
    chigh = 0
    cmedium = 0
    clow = 0
    ihigh = 0
    imedium = 0
    ilow = 0
    for i in incomplete:
        if i == 'High':
            ihigh += 1
        elif i == 'Medium':
            imedium += 1
        elif i == 'Low':
            ilow += 1
    for i in complete:
        if i == 'High':
            chigh += 1
        elif i == 'Medium':
            cmedium += 1
        elif i == 'Low':
            clow += 1
    print(f"No. of incomplete tasks is {len(incomplete)} (High={ihigh}, Medium={imedium}, Low={ilow})")
    print(f"No. of incomplete tasks is {len(complete)} (High={chigh}, Medium={cmedium}, Low={clow})")
    print()

def removeTask():
    print("---- ---- ---- ---- ---- ---- ----")
    index = input("Enter task index: ")
    while int(index) > len(alltask):
        print("Error: Index not found. Please type again.")
        print()
        index = int(input("Enter task index: "))
    print(f"{alltask[int(index)][0]} removed!")
    del alltask[int(index)]
    print()

def markCompletes():
    print("---- ---- ---- ---- ---- ---- ----")
    count = 0
    for task in alltask:
        if task[2] == 'I':
            task[2] = 'C'
            count += 1
            print(f"{task[0]} completed at {getTime()}")
    if count == 0:
        print("No incomplete tasks")
    print()