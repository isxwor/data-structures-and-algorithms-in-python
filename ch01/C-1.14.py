''' C-1.14
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''


# Since, the product of odd numbers is odd, we check if there is atleast 
# two odd numbers in the sequence
def has_pair(seq):
    s = list(set(seq)) # remove duplicates
    count = 0
    for n in s:
        if n % 2 == 1:
            count += 1
        if count == 2:
            return True
    return False


if __name__ == '__main__':
    seq = [2, 3, 4, 7, 8]
    result = has_pair(seq)
    print(result)
