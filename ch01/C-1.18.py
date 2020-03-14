''' C-1.18
Demonstrate how to use Python’s list comprehension syntax to produce
the list[0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
'''

list = [k*(k+1) for k in range(10)]
print(list)
