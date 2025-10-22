def find_position(sorted_list, new_value):
    for i in range(len(sorted_list)):
        if new_value <= sorted_list[i]:
            return i
    return len(sorted_list)

cont = False
while cont == False:
    g=0
    numbers = [1, 3, 5, 7, 9]
    print("Список:", numbers)
    new_value = int(input("Введіть число для вставки: "))
    pos = find_position(numbers, new_value)
    numbers.insert(pos, new_value)
    print("Число вставлено на позицію:", pos)
    print("Новий список:", numbers)
    while g == 0:        
        d = input("Бажаєте продовжити? (yes/no)")
        if d == "yes":
            cont = False
            g = 1
        elif d == "no":
            cont = True
            g = 1
        else:
            print("Введіть yes або no")


