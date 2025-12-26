import logging

def setup_logger():
    logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_operation(a, b, operation, result):
    logging.info(f'Операції: a={a}, b={b}, operation={operation}, result={result}')

def log_error(message):
    logging.error(f"Помилка: {message}")