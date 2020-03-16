''' C-2.25
Exercise R-2.12 uses the __mul__ method to support multiplying a Vector by a number, while Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors. Give a single implementation of Vector.__mul__ that uses run-time type checking to support both syntaxes u * v and u * k, where u and v designate vector instances and k represents a number.
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
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        else:
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
    u = [0, 0, 2, 0, 1]
    k = 3
    print(v * k)
    print(v * u)
