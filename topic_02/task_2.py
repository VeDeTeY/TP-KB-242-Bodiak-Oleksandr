
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

# головна програма
print("Простий калькулятор")
print("Операції:")
print("1. Додавання (+)")
print("2. Віднімання (-)")
print("3. Множення (*)")
print("4. Ділення (/)")

choice = input("Оберіть операцію (+, -, *, /): ")

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if choice == "+":
    print("Результат:", plus(a, b))
elif choice == "-":
    print("Результат:", minus(a, b))
elif choice == "*":
    print("Результат:", multiply(a, b))
elif choice == "/":
    print("Результат:", divide(a, b))
else:
    print("Неправильний вибір операції!")
