''' R-2.23
In similar spirit to the previous problem, augment the Sequence class with
method __lt__, to support lexicographic comparison seq1 < seq2.
'''


from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
       pass
    
    @abstractmethod
    def __getitem__(self, j):
        pass
    
    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    
    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
    
    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False  # must have equal lengths
        else:
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
    
    def __lt__(self, other):
        for i in range(min(len(self), len(other))):
            if self[i] < other[i]:
                return True
        return False


if __name__ == '__main__':
    # ------ Tests ------
    class Test(Sequence):
        ''' Dummy class for testing our Sequence Abstract Base Class
        
        Since, our goal is to test the functionality of new methods of
        our Sequence ABC, I've not implemented proper __len__ and __getitem__
        methods for this. So, they rely on respective methods of Python's
        built-in list class.
        '''
        def __init__(self, values):
            self._values = values
            self._length = len(values)
        
        def __len__(self):
            return self._length
        
        def __getitem__(self, j):
            return self._values[j]
    
    
    seq1 = Test([2, 4, 1, 2])
    seq2 = Test([2, 4, 1, 3])
    
    print(seq1 < seq2)
