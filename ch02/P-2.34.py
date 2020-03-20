''' P-2.34
Write a Python program that inputs a document and then outputs a bar
chart plot of the frequencies of each alphabet character that appears in
that document.
'''

import matplotlib.pyplot as plt


def document_reader(file):
    freq = {chr(key): 0 for key in range(97, 123)}  # lowercase a to z
    
    with open(file) as f:
        lines = (line.strip().lower() for line in f)
        for line in lines:
            for char in line:
                if char.isalpha():
                    freq[char] += 1
    
    index = range(len(freq))
    label = list(freq.keys())
    n = list(freq.values())
    
    plt.title('Frequencies Of Alphabet Characters')
    plt.bar(index, n, align='center')
    plt.xticks(index, label)
    plt.xlabel('Alphabet Characters')
    plt.ylabel('Frequencies')
    plt.show()


if __name__ == '__main__':
    filepath = 'sample_files/document.txt'
    document_reader(filepath)
