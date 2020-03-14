''' C-1.15
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''

# ---- SOLUTION ONE ---
def are_distinct_1(seq):
    for i, n in enumerate(seq):
        if n in seq[i+1:]:
            return False
    return True

# ---- SOLUTION TWO ----
def are_distinct_2(seq):
    s = set(seq)           # remove duplicates
    if len(seq) == len(s): # should be equal if numbers are distinct
        return True
    return False


if __name__ == '__main__':
    seq = [1, 2, 3, 4]
    
    result_1 = are_distinct_1(seq)
    result_2 = are_distinct_2(seq)
    
    print('Solution 1:', result_1)
    print('Solution 2:', result_2)
