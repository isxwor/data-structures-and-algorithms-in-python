''' C-4.12
Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.
'''

def product(m, n):
    if m > 1:
        return n + product(m-1, n)
    else:
        return n


if __name__ == '__main__':
    mn = list(map(int, input('Enter any two integers [space seperated]: ').split()))
    result = product(*mn)
    print(result)
