''' C-4.22
Develop a nonrecursive implementation of the version of power from
Code Fragment 4.12 that uses repeated squaring.
'''

# -- Solution one --
def power(x, n):
    result = 1
    while n > 0:
        while n % 2 == 0:
            n /= 2
            x *= x
        n -= 1
        result *= x
    return result

# -- Solution two --
def _power(x, n):
    factor = n
    partial = 1
    counter = 0
    while factor:
        factor = factor >> 1
        counter += 1
    while counter+1:
        partial *= partial
        if (n >> counter) & 1:
            partial *= x
        counter -= 1
    return partial


if __name__ == '__main__':
    xn = list(map(int, input('Enter base and exponent [space seperated]: ').split()))
    print(power(*xn))
    print(_power(*xn))
