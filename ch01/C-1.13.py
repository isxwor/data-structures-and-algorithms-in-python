''' C-1.13
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''

def _reverse(list):
    temp = []
    for i in range(len(list) - 1, -1, -1):
        temp.append(list[i])
    return temp


if __name__ == '__main__':
    list = [1,2,3,4,5] 
    print(_reverse(list))
    	
    # The Python function does not need to
    # be passed the value of n as an argument.
    list.reverse()
    print(list)
