# hello.py - simple greeting script

def greet():
    name = input('Enter your name: ').strip()
    if not name:
        print('No name entered. Please try again.')
        return
    print(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
