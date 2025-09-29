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

print("Калькулятор")
print(" Виберіть операцію: +, -, *, /")
print("Щоб завершити програму, напишіть 'exit' або 'вихід'")

while True:
    choice = input("\nОберіть операцію (+, -, *, /): ")
    
    if choice.lower() in ["exit", "вихід"]:
        print("Роботу закінчено")
        break
    
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: потрібно вводити числа!")
        continue
    
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
            
