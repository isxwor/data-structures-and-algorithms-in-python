''' C-1.20
Python’s random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function.
'''

from random import randint


def shuffle(data):
    for n in range(0, len(data)):
        i = randint(0, n)
        data[n], data[i] = data[i], data[n]
		

if __name__ == '__main__':
    list = [1,2,3,4]
    shuffle(list)
    print(list)
