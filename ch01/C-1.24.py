''' C-1.24
Write a short Python function that counts the number of vowels in a given
character string.
'''


def num_vowel(string):
    count = 0
    for c in string.lower():
        if c in 'aeiou':
            count += 1
    return count


if __name__ == '__main__':
    string = 'Hello!'
    result = num_vowel(string)
    print(result)
