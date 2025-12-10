from sys import argv
import csv

##################### PRINT LIST ##########################
def printAllList(student_list):
    for elem in student_list:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Group: {elem['group']}")
    print("====================================")
    return


##################### Створення нового списку ##########################
def addNewElement(student_list):
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    group = input("Enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    ################ Знаходжкння позиції для вставлення ########################
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    student_list.insert(insertPosition, newItem)
    print("New student added.")
    return


##################### Видалення інформації ##########################
def deleteElement(student_list):
    name = input("Enter student name to delete: ")
    deletePosition = -1

    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break

    if deletePosition == -1:
        print("Student not found.")
    else:
        del student_list[deletePosition]
        print("Student deleted.")
    return


##################### Оновлення інформації ##########################
def updateElement(student_list):
    name = input("Enter student name to update: ")
    deletePosition = -1

    ################ Знаходження студента для оновлення ##################
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break

    if deletePosition == -1:
        print("Student not found.")
    else:
        #################### видалення старого запису із списку ####################
        del student_list[deletePosition]

        print("Введіть нові дані:")
        name = input("Enter student name: ")
        phone = input("Enter student phone: ")
        email = input("Enter student email: ")
        group = input("Enter student group: ")

        newItem = {"name": name, "phone": phone, "email": email, "group": group}

        # insert back in sorted order
        insertPosition = 0
        for item in student_list:
            if name > item["name"]:
                insertPosition += 1
            else:
                break

        student_list.insert(insertPosition, newItem)
        print("Student updated.")

    return


##################### MAIN ##########################
def main():
    student_list = []

    filename = "lab_02.csv"

    # Load CSV
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            csvFile = csv.DictReader(file)
            for line in csvFile:
                student_list.append({
                    "name": line['name'],
                    "phone": line['phone'],
                    "email": line['email'],
                    "group": line['group']
                })
    except FileNotFoundError:
        print("Файл lab_02.csv не знайшовся.")

    ################################
    while True:
        choice = input("Choose: [C create, U update, D delete, P print, X exit] ")

        match choice:
            case "C" | "c":
                print("\nCreating new student:")
                addNewElement(student_list)
                printAllList(student_list)

            case "U" | "u":
                print("\nUpdating student:")
                updateElement(student_list)
                printAllList(student_list)

            case "D" | "d":
                print("\nDeleting student:")
                deleteElement(student_list)
                printAllList(student_list)

            case "P" | "p":
                print("\nStudent list:")
                printAllList(student_list)

            case "X" | "x":
                print("\nSaving data and exiting...")
                break

            case _:
                print("Wrong choice.")

    ############# збереження у ajhvfns CSV ###############
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        fieldnames = ['name', 'phone', 'email', 'group']
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for elem in student_list:
            writer.writerow({
                'name': elem["name"],
                'phone': elem["phone"],
                'email': elem["email"],
                'group': elem["group"]
            })

    print("Data saved. Goodbye!")


if __name__ == "__main__":
    main()
