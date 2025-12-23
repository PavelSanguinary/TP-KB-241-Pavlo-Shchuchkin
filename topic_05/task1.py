#import random

import random

value = random.choice(["stone", "scissor", "paper"])
a = input('Виберіть stone, scissor or paper: ')
print("Ви обрали: ", a, ", Бот обрав: ", value) 
if a not in ["stone", "scissor", "paper"]:
    print("Невірне значення")
elif value == a:
    print("Нічия")
elif (value == "stone" and a == "scissor") or (value == "scissor" and a == "paper") or (value == "paper" and a == "stone"):
    print("Ви програли")
else:
    print("Ви перемогли!")
