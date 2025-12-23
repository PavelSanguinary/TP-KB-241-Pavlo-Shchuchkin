from functions import plus, minus, mnoj, dilena

def input_numbers():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    return a, b

def input_operation():
    return input("Виберіть операцію (+-*/): ")

def do_operation(a, b, f):
    if f == '+':
        return plus(a, b)
    elif f == '-':
        return minus(a, b)
    elif f == '*':
        return mnoj(a, b)
    elif f == '/':
        return dilena(a, b)
    else:
        return "Невірно введена операція"

def run_calculator():
    a, b = input_numbers()
    f = input_operation()
    result = do_operation(a, b, f)
    print(result)
