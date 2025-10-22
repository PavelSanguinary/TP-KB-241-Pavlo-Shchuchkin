def plus(a,b):
    c = a+b
    return c

def minus(a,b):
    c = a-b
    return c
def dilena(a,b):
    c = a/b
    return c
def mnojena(a,b):
    c=a*b
    return c

cont = False
while cont == False:
    g = 0
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    f = input('Enter operation (+-*/): ')
    match f:
        case '+':
            print(plus(a,b))
        case '-':
            print(minus(a,b))
        case '/':
            if b == 0:
                print("Помилка")
            else:
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