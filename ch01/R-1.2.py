''' R-1.2
Write a short Python function, is even (k), that takes an integer value and 
returns True if k is even, and False otherwise. However, your function 
cannot use the multiplication, modulo, or division operators.
'''

def is_even(k):
    return k & 1 == 0


if __name__ == '__main__':
    k = int(input('Enter a number: '))
    check = is_even(k)
    print(check)
