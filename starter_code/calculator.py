# calculator.py - basic arithmetic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

if __name__ == '__main__':
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
    except Exception:
        print('Invalid input. Please enter numbers.')
    else:
        print('Add:', add(a, b))
        print('Subtract:', subtract(a, b))
        print('Multiply:', multiply(a, b))
        q = divide(a, b)
        if q is None:
            print('Divide: Error (division by zero)')
        else:
            print('Divide:', q)
