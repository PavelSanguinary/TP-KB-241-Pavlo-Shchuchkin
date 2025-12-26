# calculator.py
from operation import plus, minus, mnoj, dilena
from log import setup_logger, log_operation, log_error

class Calculator:
    def __init__(self):
        setup_logger()  
        self.result = 0
    def input_numbers(self):
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            print("Неправильно введено значення.")
            log_error("НЕправильне значення")
            return None, None

    def input_operation(self):
        operation = input("Виберіть операцію (+, -, *, /): ")
        if operation not in ('+', '-', '*', '/'):
            print("Неправильна операція!")
            log_error(f"Неправильна операція: {operation}")
            return None
        return operation

    def do_operation(self, a, b, operation):
        if operation == '+':
            result = plus(a, b)
        elif operation == '-':
            result = minus(a, b)
        elif operation == '*':
            result = mnoj(a, b)
        elif operation == '/':
            result = dilena(a, b)
        else:
            result = ""

        log_operation(a, b, operation, result)
        return result

    def run(self):
        a, b = self.input_numbers()
        if a is None or b is None:
            return 

        operation = self.input_operation()
        if operation is None:
            return  

        result = self.do_operation(a, b, operation)
        print("Result:", result)
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
