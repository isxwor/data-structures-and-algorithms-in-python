''' P-1.30
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
'''

# --- Using the log function ---
def _log2(n):
    if n >= 2:
        from math import log
        return int(log(n, 2))


# ------ Using recursion -------
def rec_div2(n):
    if n < 2:
        return 0
    else:
        return 1 + rec_div2(n // 2)


# ------ Using while loop ------
def while_div2(n):
    counter = 0
    while n >= 2:
        counter += 1
        n /= 2
    return counter


if __name__ == '__main__':
    n = int(input('Enter integer greater than 2: '))
    
    print(_log2(n))
    print(rec_div2(n))
    print(while_div2(n))
