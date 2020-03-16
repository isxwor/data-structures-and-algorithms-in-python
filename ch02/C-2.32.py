''' C-2.32
Write a Python class that extends the Progression class so that each value
in the progression is the square root of the previous value. (Note that
you can no longer represent each value with an integer.) Your constructor
should accept an optional parameter specifying the start value, using
65,536 as a default.
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


class SqrtProgression(Progression):
    def __init__(self, start=65536):
        super().__init__(start)
	
    def _advance(self):
        self._current **= (1/2)


if __name__ == '__main__':
    SqrtProgression().print_progression(5)
