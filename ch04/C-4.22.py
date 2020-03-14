''' C-4.22
Develop a nonrecursive implementation of the version of power from
Code Fragment 4.12 that uses repeated squaring.
'''

def power(x, n):
    result = 1
    while n > 0:
        while n % 2 == 0:
            n /= 2
            x *= x
        n -= 1
        result *= x
    return result


if __name__ == '__main__':
    xn = list(map(int, input('Enter base and exponent [space seperated]: ').split()))
    test = power(*xn)
    print(test)
