class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"


################## Список студентів ##################
students = [
    Student("Oleh", 17),
    Student("Dima", 18),
    Student("Max", 20),
    Student("Alex", 19),
]

column = input("Введіть поле для сортування (name / age): ")

###################### Перевірка на коректність введеного поля ####################
if column not in ("name", "age"):
    print("Некоректне поле!")
else:
    ################## Сортування за допомогою lambda + getattr ##################
    sorted_students = sorted(students, key=lambda item: getattr(item, column))

    print("\n Відсортований список:")
    for student in sorted_students:
        print(student)
