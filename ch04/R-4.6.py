''' R-4.6
Look book for the question of this solution.
'''


def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


if __name__ == '__main__':
    n = 4
    result = harmonic(n)
    print(result)
