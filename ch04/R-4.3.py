''' R-4.3
Draw the recursion trace for the computation of power(2,18), using the
repeated squaring algorithm, as implemented in Code Fragment 4.12.
'''


def power(x, n):
    '''Compute the value x**n for integer n.'''
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


print(power(2, 18))

''' The recursion trace for the computation of power(2, 18) is,

               return 512 * 512 = 262144
power(2, 18)
                  return 16 * 16 * 2 = 512
    power(2, 9)
                      return 4 * 4 = 16
        power(2, 4)
                          return 2 * 2 = 4
            power(2, 2)
                              return 1 * 1 * 2 = 2
                power(2, 1)
                                  return 1
                    power(2, 0)
'''
