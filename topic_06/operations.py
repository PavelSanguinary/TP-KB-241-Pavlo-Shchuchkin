from functions import plus, minus, mnoj, dilena
import logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')
def input_numbers():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    return a, b

def input_operation():
    return input("Виберіть операцію (+-*/): ")

def do_operation(a, b, f):
    if f == '+':
        result = plus(a, b)
        log_operation(a, b, '+', result)
        return result
    elif f == '-':
        result = minus(a, b)
        log_operation(a, b, '-', result)  
        return result
    elif f == '*':
        result = mnoj(a, b)
        log_operation(a, b, '*', result)  
        return result
    elif f == '/':
        result = dilena(a, b)
        log_operation(a, b, '/', result) 
        return result
    else:
        error_message = "Невірно введена операція"
        log_operation(a, b, f, error_message) 
        return error_message

def run_calculator():
    a, b = input_numbers()
    f = input_operation()
    result = do_operation(a, b, f)
    print(result)

def log_operation(a, b, operation, result):
    logging.info(f'User input: a={a}, b={b}, operation={operation}, result={result}')