''' C-2.26
The SequenceIterator class of Section 2.3.4 provides what is known as a
forward iterator. Implement a class named ReversedSequenceIterator that
serves as a reverse iterator for any Python sequence type. The ﬁrst call to
next should return the last element of the sequence, the second call to next
should return the second-to-last element, and so forth.
'''

class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)
    
    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self


if __name__ == '__main__':
    seq = ReversedSequenceIterator(['a', 2, 'c', 3])
    rev = [x for x in seq]
    print(rev)
