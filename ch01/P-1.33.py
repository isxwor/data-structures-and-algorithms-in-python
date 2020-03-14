''' P-1.33
Write a Python program that simulates a handheld calculator. Your program
should process input from the Python console representing buttons that are
“pushed,” and then output the contents of the screen after each operation
is performed. Minimally, your calculator should be able to process the basic
arithmetic operations and a reset/clear operation.
'''


import os


def header():
    print('-------- Simple Calculator --------')
    print('Available operators:\n\
    + for addition\n\
    - for subtraction\n\
    * for multiplication\n\
    / for division\n\
    r for reset/clear\n\
[ctrl + d to quit.]')
    print('-' * 36)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
	
def calculator():
    query = ''
    while True:
        try:
            cmd = input()
            if cmd == 'r':
                query = ''
                clear()
            else:
                query += cmd
                query = str(eval(query))
                print('=', query)
        except EOFError:
            break


if __name__ == '__main__':
    header()
    calculator()
