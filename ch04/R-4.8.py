''' R-4.8
Isabel has an interesting way of summing up the values in a sequence A of
n integers, where n is a power of two. She creates a new sequence B of half
the size of A and sets B[i] = A[2i]+A[2i+1], for i = 0,1,...,(n/2)−1. If
B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
repeats the process. What is the running time of her algorithm?
'''

import math


def isabel_method(A):
    if math.log(len(A), 2) % 1 != 0:
        raise ValueError('length of an array is not a power of two')
    if len(A) == 1:
        return A[0]
    else:
        B = [None] * (len(A)//2)
        for i in range(len(B)):
            B[i] = A[2*i] + A[2*i+1]
        return isabel_method(B)


A = [1, 2, 5, 2, 8, 6, 0, 9]
result = isabel_method(A)
print(result)

# Running time is O(n)
