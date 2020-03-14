''' P-1.36
Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You need not to
worry about efﬁciency at this point, however, as this topic is
something that will be addressed later in this book.
'''

def count_1(list):
    counted = {}
    for word in list:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    return counted
	
# ---- Using Built-in function ----
def count_2(list):
    from collections import Counter
    counted = Counter(list)
    return counted


if __name__ == '__main__':
    list = input('Enter words (seperated by whitespace):\n').lower().split()
    
    result = count_1(list)
    # result = count_2(list)
    for word, occurence in result.items():
        print(f'{word}: {occurence}')
