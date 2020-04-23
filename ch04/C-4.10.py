''' C-4.10
Describe a recursive algorithm to compute the integer part of the base-two
logarithm of n using only addition and integer division.
'''


def calc(n):
    if n < 2:
        return 0
    else:
        return 1 + calc(n // 2)


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(calc(n))
