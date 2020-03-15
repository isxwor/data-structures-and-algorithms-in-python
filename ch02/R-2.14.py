''' R-2.14
Implement the __mul__ method for the Vector class of Section 2.3.3, so that
the expression u * v returns a scalar that represents the dot product of the
vectors.
'''

class Vector:
    def __init__(self, d):
        self._coords = [0] * d
    
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
    v = Vector(5)
    v[1] = 4
    v[-1] = 2
    v[3] = 1
    u = [0, 0, 2, 0, 1]
    print(u * v)
