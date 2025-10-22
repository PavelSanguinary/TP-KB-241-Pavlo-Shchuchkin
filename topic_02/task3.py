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