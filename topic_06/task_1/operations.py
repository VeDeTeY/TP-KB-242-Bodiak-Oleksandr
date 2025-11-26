from functions import add, subtract, multiply, divide
from log import log_operation, log_error, log_warning

def numbers():
    """Функція для введення чисел з обробкою помилок"""
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            print("Помилка! Введіть коректне число.")
            log_warning("Помилка введення: користувач ввів некоректні дані")

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
        log_warning(f"Невірний вибір операції: {choice}")
        return
    
    operation_name, operation_func = operations[choice]
    a, b = numbers()
    
    result = operation_func(a, b)
    
    # Виведення результату
    print(f"Результат: {result}")
    
    # Логування операції
    if isinstance(result, str):  # Якщо помилка (ділення на нуль)
        log_error(operation_name, a, b, result)
    else:
        log_operation(operation_name, a, b, result)