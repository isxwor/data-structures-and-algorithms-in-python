''' C-4.16
Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of 'pots&pans' would be 'snap&stop'.
'''


def flip(s, n=0):
    if n == len(s)-1:
        return s[n]
    return flip(s, n+1) + s[n]


if __name__ == '__main__':
    s = list(input('Enter any strings: '))
    result = flip(s)
    print(result)
