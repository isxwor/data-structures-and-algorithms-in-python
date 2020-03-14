''' C-4.17
Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, 'racecar' and
'gohangasalamiimalasagnahog' are palindromes.
'''

def palindrome(s, n):
    if n <= 1:
        return True
    else:
        if s[n-1] == s[-n]:
            return palindrome(s, n-1)
        return False


if __name__ == '__main__':
    s = input('Enter any word: ')
    n = len(s) // 2
    test = palindrome(s, n)
    print(test)
