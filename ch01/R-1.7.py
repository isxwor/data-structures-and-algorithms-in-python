''' R-1.7
Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
'''

n = 12
total = sum(i*i for i in range(1, n+1, 2))
print(total)
