def dict_testing():

    student = {"name": "Alex", "age": 20, "grade": "A"}
    print("Початковий словник:", student)
    
    # update()
    student.update({"age": 21, "city": "Kyiv"})
    print("Результат після update({'age': 21, 'city': 'Kyiv'}):", student)
    
    # del
    del student["grade"]
    print("Результат після del student['grade']:", student)
    
    # keys()
    print("Ключі:", list(student.keys()))
    
    # values()
    print("Значення:", list(student.values()))
    
    # items()
    print("Пари ключ:значення:", list(student.items()))
    
    # clear()
    student.clear()
    print("Результат після clear():", student)

dict_testing()
