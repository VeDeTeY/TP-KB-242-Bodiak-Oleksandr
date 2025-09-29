import math
def discr(a, b, c):
    d = b**2 - 4*a*c
    return d
# функція для пошуку коренів
def quadro(a, b, c):
    d = discr(a, b, c) # виклик функції для обчислення дискримінанта
    print(f"Дискримінант = {d}")
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Два корені: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Один корінь: x = {x}"
    else:
        return "Коренів немає (дискримінант < 0)"

# введення даних
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# виклик функції
print(quadro(a, b, c))
