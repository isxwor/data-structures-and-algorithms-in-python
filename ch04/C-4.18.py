''' C-4.18
Use recursion to write a Python function for determining if a string s has
more vowels than consonants.
'''

def hasMoreVowels(s, n, c=0):
    v = ['a', 'e', 'i', 'o', 'u']
    if n < 0:
        return c > 0
    else:
        c += 1 if s[n] in v else -1
        return hasMoreVowels(s, n-1, c)


if __name__ == '__main__':
    s = input('Enter any string: ')
    result = hasMoreVowels(s, len(s)-1)
    print(result)
