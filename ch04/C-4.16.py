''' C-4.16
Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of 'pots&pans' would be 'snap&stop'.
'''

def flip(s, n):
    if n == 0:
        return s[n]
    return s[n] + flip(s, n-1)


if __name__ == '__main__':
    s = list(input('Enter any strings: '))
    n = len(s) - 1
    result = flip(s, n)
    print(result)
