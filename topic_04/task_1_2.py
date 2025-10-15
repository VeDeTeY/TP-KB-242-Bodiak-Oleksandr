
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

#########Функція ділення з обробкою винятку#################
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError: ##############Обробка ділення на нуль###################
        return "Помилка: ділення на нуль неможливе!"


##############Функція введення чисел із перевіркою###############
def get_numbers():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError: ##############Обробка некоректного вводу#########
            print("Помилка: потрібно вводити тільки числа! Спробуйте ще раз.\n")


#Основна програма
print("Простий калькулятор")
print("Операції: +, -, *, /")
print("Для виходу введіть 'exit'\n")

while True:
    choice = input("Оберіть операцію (+, -, *, / або 'exit'): ")

    if choice.lower() == "exit":
        print("Роботу завершено. До побачення!")
        break

    if choice not in ["+", "-", "*", "/"]:
        print("Неправильний вибір операції! Спробуйте ще раз.\n")
        continue

    a, b = get_numbers()

    match choice:
        case "+":
            print("Результат:", plus(a, b))
        case "-":
            print("Результат:", minus(a, b))
        case "*":
            print("Результат:", multiply(a, b))
        case "/":
            print("Результат:", divide(a, b))

    print() 
