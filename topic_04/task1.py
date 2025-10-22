def plus(a,b):
    c = a+b
    return c
def genIntValue(promt:str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Неправильне значення")

def minus(a,b):
    c = a-b
    return c
def dilena(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError:
        print("Ділити на нуль не можна")
def mnojena(a,b):
    c=a*b
    return c

cont = False
while cont == False:
    g = 0
    try:
        a = genIntValue("Enter first number: ")
        b = genIntValue("Enter second number: ")
    except ValueError:
        print("Введіть правильне значення")
    f = input('Enter operation (+-*/): ')
    match f:
        case '+':
            print(plus(a,b))
        case '-':
            print(minus(a,b))
        case '/':
                print(dilena(a,b))
        case '*':
            print(mnojena(a,b))
        case _:
            print("Невірно введена операція")
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