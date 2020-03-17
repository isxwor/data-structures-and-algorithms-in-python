''' P-2.33
Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the ﬁrst derivative of that polynomial.
'''

class Polynomial:
    ''' A class to represent polynomial in standard algebraic notation
    
    Supports polynomial in a single indeterminate only '''
    def __init__(self, *coefficients):
        self._coeffs = list(coefficients)
    
    def __len__(self):
        return len(self._coeffs)
    
    def __getitem__(self, k):
        return self._coeffs[k]
    
    def __str__(self):
        degree = len(self) - 1
        result = f'{self[0]}x^{degree}'
        for i in range(1, len(self)-1):
            if self[i] < 0:
                result += f' - {-self[i]}x^{degree-i}'
            else:
                result += f' + {self[i]}x^{degree-i}'
        if self[-1] < 0:
            result += f' - {-self[-1]}'
        else:
            result += f' + {self[-1]}'
        return result
    
    def derivative(self):
        derived_coeffs = []
        exponent = len(self) - 1
        for i in range(len(self)-1):
            derived_coeffs.append(self[i]*exponent)
            exponent -= 1
        return Polynomial(*derived_coeffs)


if __name__ == '__main__':
    p = Polynomial(-7, 280, -2)
    print(p)
    pd = p.derivative()
    print(pd)
