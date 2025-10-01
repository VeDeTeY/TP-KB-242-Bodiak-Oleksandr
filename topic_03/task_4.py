fruits = ["apple", "cherry", "melon"]
new_fruit = input("Введіть новий фрукт: ")

def find_position(sorted_list, new_item):
    # проходження по елементах із списку
    for i in range(len(sorted_list)):
        # якщо новий елемент "менший" за поточний — вставляти сюди
        if new_item < sorted_list[i]:
            return i
    # якщо більший за всі — вставляється в кінець списку 
    return len(sorted_list)

pos = find_position(fruits, new_fruit)
fruits.insert(pos, new_fruit)

print("Позиція для вставки:", pos)
print("Новий список:", fruits)
