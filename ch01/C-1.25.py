''' C-1.25
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
'''

import string


# ---- SOLUTION ONE ----
def no_punctuation_1(data):
    res = data.translate(str.maketrans('', '', string.punctuation))
    return res

# ---- SOLUTION TWO ----
def no_punctuation_2(data):
    exclude = string.punctuation
    res = ''.join(x for x in data if x not in exclude)
    return res

if __name__ == '__main__':
    data = 'Let\'s try, Mike.'
    result_1 = no_punctuation_1(data)
    result_2 = no_punctuation_2(data)
    
    print('Solution 1:', result_1)
    print('Solution 2:', result_2)
