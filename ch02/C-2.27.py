''' C-2.27.py
In Section 2.3.5, we note that our version of the Range class has implicit
support for iteration, due to its explicit support of both __len__
and __getitem__. The class also receives implicit support of the Boolean
test, “k in r” for Range r. This test is evaluated based on a forward iteration
through the range, as evidenced by the relative quickness of the test
2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
more efﬁcient implementation of the __contains__ method to determine
whether a particular value lies within a given range. The running time of
your method should be independent of the length of the range.
'''


# modified from original book's implementation
# to provide better functionality
class Range:
    ''' A class that mimic's the built-in range class '''
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self._start = start
        self._stop = stop
        self._step = step
        if step > 0:
            lo, hi = start, stop
        elif step < 0:
            lo, hi, step = stop, start, -step
        else:
            raise ValueError('step cannot be 0')
        self._length = max(0, ((hi - lo - 1) // step) + 1)
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step
    
    def __iter__(self):
        current = self._start
        if self._step < 0:
            while current > self._stop:
                yield current
                current += self._step
        else:
            while current < self._stop:
                yield current
                current += self._step
    
    def __contains__(self, k):
        ''' Efficient method to return Boolean value for test 'k in r' for Range(r) '''
        if self._step < 0:
            if not (self._stop < k <= self._start):
                return False
        else:
            if not (self._start <= k < self._stop):
                return False
        return (k - self._start) % self._step == 0


if __name__ == '__main__':
    query = int(input('Enter value to test: '))
    query_range = list(map(int, input('Select range [space seperated]: ').split()))
    test = query in Range(*query_range)
    print(test)
