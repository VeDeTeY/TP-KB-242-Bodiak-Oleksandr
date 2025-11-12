import random

################### Варіанти #######################
variants = ["stone", "scissor", "paper"]

################### Введення вибору користувача ####################      
your_choice = input("Введіть свій вибір (stone, scissor, paper): ").lower()

################### Перевірка коректності введення ####################
if your_choice not in variants:
    print("Помилка: введіть лише stone, scissor або paper")
else:
    ################ Випадковий вибір комп’ютера #################
    random_choice = random.choice(variants)
    print("Комп’ютер обрав:", random_choice)

    ###################### Визначення переможця ######################
    if your_choice == random_choice:
        print("Нічия,переможців немає!")
    elif (your_choice == "stone" and random_choice == "scissor") or \
         (your_choice == "scissor" and random_choice == "paper") or \
         (your_choice == "paper" and random_choice == "stone"):
        print("Ви перемогли!")
    else:
        print("Ви програли!")