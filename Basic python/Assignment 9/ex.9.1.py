def MyBio(name, surname, age):
    if age < 5 or age > 70:
        print(f"Dear {name} {surname}, you should stay home to avoid Covid-19.")
    else:
        print(f"Dear {name} {surname}, please stay home as much as you can.")

name=input("Enter firstname: ")
surname=input("Enter surname: ")
age=int(input("Enter age: "))
MyBio(name,surname,age)