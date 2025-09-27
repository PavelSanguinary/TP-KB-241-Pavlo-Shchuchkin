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
if f == '+':
    print(plus(a,b))
elif f == '-':
    print(minus(a,b))
elif f == '/':
    print(dilena(a,b))
elif f == '*':
    print(mnojena(a,b))
else:
    print("Невірно введена операція")