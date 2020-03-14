''' R-1.3
Write a short Python function, minmax (data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
'''

def minmax(data):
    small = big = data[0]
    for val in data:
        if val < small:
            small = val
        elif val > big:
            big = val
    return small, big
		
	
if __name__ == '__main__':
    data = [2,8,1,4]
    result = minmax(data)
    print(result)
