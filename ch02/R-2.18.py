''' R-2.18
Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to ﬁnd the 8th value of a Fibonacci progression that
starts with 2 and 2 as its ﬁrst two values.
'''


class Progression:
    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        self._current += 1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class FibonaciiProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first
    
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
    
    def __getitem__(self, k):
        previous = self._prev
        current = self._current
        for _ in range(k):
            answer = next(self)
        self._prev, self._current = previous, current
        return answer


if __name__ == '__main__':
    f = FibonaciiProgression(2, 2)
    print(f[8])
    f.print_progression(10)
