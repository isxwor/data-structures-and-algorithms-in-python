''' R-4.7
Describe a recursive function for converting a string of digits into the
integer it represents. For example, 13531 represents the integer 13,531.
'''


def str_to_int(s, index=0):
    length = len(s)-1
    if index == length:
        return int(s[index])
    else:
        return int(s[index])*pow(10, length-index) + str_to_int(s, index+1)


if __name__ == '__main__':
    s = '13531'
    result = str_to_int(s)
    print(result, type(result))

