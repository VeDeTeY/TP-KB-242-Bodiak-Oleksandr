import bisect

# Початковий відсортований список
fruits = ["apple", "cherry", "durian"]
print("Початковий список:", fruits)

new_fruit = input("Введіть фрукт: ")

# Знаходимо позицію для вставки нового фрукта #
pos = bisect.bisect_left(fruits, new_fruit)

# Вставляємо новий фрукт у правильне місце #
fruits.insert(pos, new_fruit)

print("Позиція для вставки:", pos)
print("Новий список:", fruits)
