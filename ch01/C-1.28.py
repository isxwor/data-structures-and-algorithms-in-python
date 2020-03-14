''' C-1.28
Look book for the question of this solution.
'''

def norm(v, p=2):
    temp = sum(abs(x)**p for x in v)
    return round(temp**(1/p), 2)


if __name__ == '__main__':
    v = [4, 3]
    euclidean_norm = norm(v)
    print('Euclidean norm:', euclidean_norm)
    
    p_norm = norm(v, 3)
    print('p-norm: ', p_norm)
