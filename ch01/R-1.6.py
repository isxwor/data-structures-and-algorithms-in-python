''' R-1.6
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
'''

def sum_of_squares(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i * i
    return total


if __name__ == '__main__':
    result = sum_of_squares(12)
    print(result)
