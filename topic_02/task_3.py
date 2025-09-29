
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"
    ##############################################################
print("Простий калькулятор")
print("Операції:")
print("1. Додавання (+)")
print("2. Віднімання (-)")
print("3. Множення (*)")
print("4. Ділення (/)")

choice = input("Оберіть операцію (+, -, *, /): ")

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

match choice:
    case "+":
        print("Результат:", plus(a, b))
    case "-":
        print("Результат:", minus(a, b))
    case "*":
        print("Результат:", multiply(a, b))
    case "/":
        print("Результат:", divide(a, b))
    case _:
        print("Неправильний вибір операції!")
