''' C-1.26
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c”, “a = b − c”, or “a * b = c”.
'''

def check(a, b, c):
    if (a + b == c) or (b - c == a) or (a * b == c):
        return True
    return False


if __name__ == '__main__':
    numbers = list(map(int, input(
        'Enter any 3 numbers [space seperated]:'
    ).split()))
    result = check(*numbers)
    print(result)
