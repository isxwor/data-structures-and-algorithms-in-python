''' R-2.13
Exercise R-2.12 asks for an implementation of __mul__, for the Vector
class of Section 2.3.3, to provide support for the syntax v * 3. Implement
the __rmul__ method, to provide additional support for syntax 3 * v.
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
    
    def __mul__(self, scale):
        result = Vector(len(self))
        for j in range(len(self)):
           result[j] = self[j] * scale
        return result
    
    def __rmul__(self, scale):
       return self.__mul__(scale)
    
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
    u = 3 * v
    print(u)
