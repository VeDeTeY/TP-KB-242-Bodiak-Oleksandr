from calc import Calculator

calc = Calculator()

############# Операція #############
operation = input("Виберіть операцію (+, -, *, /): ")

############## Ввід чисел ##############
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

########### Обчислення ############
result = calc.calculate(a, b, operation)

print("Результат:", result)
