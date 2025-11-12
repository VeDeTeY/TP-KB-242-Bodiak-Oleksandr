from functions import add, minus, multiply, divide

def numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def perform_operation(choice):
    a, b = numbers()
    
    if choice == '1':
        print(f"Результат: {add(a, b)}")
    elif choice == '2':
        print(f"Результат: {minus(a, b)}")
    elif choice == '3':
        print(f"Результат: {multiply(a, b)}")
    elif choice == '4':
        print(f"Результат: {divide(a, b)}")
    else:
        print("Невірний вибір!")
