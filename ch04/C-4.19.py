''' C-4.19
Write a short recursive Python function that rearranges a sequence of integer
values so that all the even values appear before all the odd values.
'''

def rearrange(s, n):
    if n == len(s):
        return s
    else:
        for i in range(n + 1, len(s)):
            if s[i] % 2 == 0 and s[n] % 2 != 0:
                s[i], s[n] = s[n], s[i]
        return rearrange(s, n+1)


if __name__ == '__main__':
    s = list(map(int, input('Enter integers [space sepersted]:\n').split()))
    n = 0
    result = rearrange(s, n)
    print(*result, sep=' ') 
