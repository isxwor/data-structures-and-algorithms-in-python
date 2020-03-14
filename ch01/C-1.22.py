''' C-1.22
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.
'''

def dot_product(a, b):
    return [x*y for x, y in zip(a, b)]
	

if __name__ == '__main__':
    a = [1, 2]
    b = [3, 4]
    result = dot_product(a, b)
    print(result)
