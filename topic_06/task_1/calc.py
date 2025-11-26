from operations import perform_operation

def main():
    while True:
        print("\nКАЛЬКУЛЯТОР")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")
        
        choice = input("Оберіть операцію (1-5): ")
        
        if choice == '5':
            print("Роботу завершено. До побачення!")
            break
        
        perform_operation(choice)

if __name__ == "__main__":
    main()