from functions import add, subtract, multiply, divide
from log import log_operation

def numbers():
    """Функція для введення чисел з обробкою помилок"""
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            print("Помилка! Введіть коректне число.")

def perform_operation(choice):
    """Виконання операції з логуванням"""
    operations = {
        '1': ('Додавання', add),
        '2': ('Віднімання', subtract),
        '3': ('Множення', multiply),
        '4': ('Ділення', divide)
    }
    
    if choice not in operations:
        print("Невірний вибір!")
        return
    
    operation_name, operation_func = operations[choice]
    a, b = numbers()
    result = operation_func(a, b)
    
    print(f"Результат: {result}")
    
    ####################### Логування  результатів ####################### 
    log_operation(operation_name, a, b, result)
