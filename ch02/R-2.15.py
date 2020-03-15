''' R-2.15
The Vector class of Section 2.3.3 provides a constructor that takes an integer d,
and produces a d-dimensional vector with all coordinates equal to 0. Another
convenient form for creating a new vector would be to send the constructor a
parameter that is some iterable type representing a sequence of numbers, and to
create a vector with dimension equal to the length of that sequence and coordinates
equal to the sequence values. For example, Vector([4, 7, 5 ]) would produce a three-
dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either
of these forms is acceptable; that is, if a single integer is sent, it produces a
vector of that dimension with all zeros, but if a sequence of numbers is provided, it
produces a vector with coordinates based on that sequence.
'''

class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            self._coords = d
    
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __mul__(self, other):
        ''' Doesn't supports multiplication with scalar.
        
        However, we'll add support for multiplication with
        both scaler and vector in C-2.25 '''
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        _sum = 0
        for i, j in zip(self, other):
            _sum += i * j
        return _sum
    
    def __rmul__(self, other):
       return self.__mul__(other)
    
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == '__main__':
    v = Vector(3)
    v[1] = 4
    v[-1] = 2
    print(v)
    u = Vector([4, 7, 5])
    print(u)
    print(u - v)
