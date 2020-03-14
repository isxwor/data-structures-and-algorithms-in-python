''' P-1.34
A common punishment for school children is to write out a sentence multiple times.
Write a Python stand-alone program that will write out the following sentence
one hundred times: “I will never spam my friends again.” Your program should number
each of the sentences and it should make eight different random-looking typos.
'''

from random import randint, shuffle, choice


def punishment():
    sentence = 'I will never spam my friends again.'
    EightTypos = []
    for i in range(8):
        EightTypos.append(sentence)
    i = 0
    while i < 8:
        s=' '
        while s is ' ':
            num = randint(0, 8*len(sentence))
            row = num // len(sentence)
            column = num % len(sentence)-1
            s = EightTypos[row][column]
        ch = chr(choice(range(97,123)))
        while ch == s:
            ch = chr(choice(range(97,123)))
        EightTypos[row] = EightTypos[row][0:column] + ch + EightTypos[row][column+1:len(sentence)]
        i += 1
    for i in range(100 - 8):
        EightTypos.append(sentence)
    shuffle(EightTypos)
    print(*EightTypos, sep='\n')
			

if __name__ == '__main__':
    punishment()
