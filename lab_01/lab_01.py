
# Початковий список студентів (уже відсортований за іменем)
students = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@gmail.com",  "group": "КБ-101"},
    {"name": "Emma", "phone": "0639876543", "email": "emma@gmail.com", "group": "КБ-102"},
    {"name": "Jon",  "phone": "0635555555", "email": "jon@gmail.com",  "group": "КБ-101"},
    {"name": "Zak",  "phone": "0631111111", "email": "zak@gmail.com",  "group": "КБ-103"}
]


############ Функція для виведення всього списку студентів#################
def printAllList():
    print("\nСПИСОК СТУДЕНТІВ:")
    for elem in students:
        print(f"Ім'я: {elem['name']}, Телефон: {elem['phone']}, Email: {elem['email']}, Група: {elem['group']}")
    print("=============================\n")
    return


############### Функція для додавання нового студента#################
def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть email студента: ")
    group = input("Введіть групу студента: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    # знайти позицію вставки для збереження сортування#################
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, newItem)
    print("Новий студент доданий.\n")
    return


#############Функція для видалення студента#################
def deleteElement():
    name = input("Введіть ім'я студента для видалення: ")
    deletePosition = -1

    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break

    if deletePosition == -1:
        print("Студента не знайдено.\n")
    else:
        del students[deletePosition]
        print("Студента видалено.\n")
    return


##########Функція для ОНОВЛЕННЯ інформації про студента#################
def updateElement():
    name = input("Введіть ім'я студента, дані якого хочете змінити: ")
    found = False

    for item in students:
        if item["name"] == name:
            found = True
            print("\nЗнайдено запис:")
            print(f"Ім'я: {item['name']}, Телефон: {item['phone']}, Email: {item['email']}, Група: {item['group']}\n")

            # Запит нових даних (Enter = залишити без змін)
            new_name = input("Нове ім'я (Enter щоб залишити): ")
            new_phone = input("Новий телефон (Enter щоб залишити): ")
            new_email = input("Новий email (Enter щоб залишити): ")
            new_group = input("Нова група (Enter щоб залишити): ")

            ########### Оновлення даних###############
            if new_name != "":
                item["name"] = new_name
            if new_phone != "":
                item["phone"] = new_phone
            if new_email != "":
                item["email"] = new_email
            if new_group != "":
                item["group"] = new_group

            ############## Зберігаємо відсортований порядок###############
            updated = item.copy()
            students.remove(item)

            insertPosition = 0
            for elem in students:
                if updated["name"] > elem["name"]:
                    insertPosition += 1
                else:
                    break
            students.insert(insertPosition, updated)

            print(" Дані студента успішно оновлено!\n")
            break

    if not found:
        print("Студента з таким ім'ям не знайдено.\n")

    return


######### Основне меню програми #################
def menu_program():
    while True:
        choice = input("Оберіть дію [C - створити, U - оновити, D - видалити, P - показати, X - вихід]: ")

        match choice:
            case "C" | "c":
                print("\n=== Додавання нового студента ===")
                addNewElement()
                printAllList()

            case "U" | "u":
                print("\n=== Оновлення інформації ===")
                updateElement()
                printAllList()

            case "D" | "d":
                print("\n=== Видалення студента ===")
                deleteElement()
                printAllList()

            case "P" | "p":
                printAllList()

            case "X" | "x":
                print(" Вихід з програми.")
                break

            case _:
                print(" Невірна команда.\n")


menu_program()
