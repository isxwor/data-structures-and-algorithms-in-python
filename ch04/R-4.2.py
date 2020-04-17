''' R-4.2
Draw the recursion trace for the computation of power(2,5), using the
traditional function implemented in Code Fragment 4.11.
'''


def power(x, n):
    '''Compute the value x**n for integer n'''
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


print(power(2, 5))

''' The recursion trace for the computation of power(2, 5) is,


              return 2 * 16 = 32
power(2, 5)
                  return 2 * 8 = 16
    power(2, 4)
                      return 2 * 4 = 8
        power(2, 3)
                          return 2 * 2 = 4
            power(2, 2)
                              return 2 * 1 = 2
                power(2, 1)
                                  return 1
                    power(2, 0)

(The arrows would trace downwards for calls and upwarfs for returns,
as in the textbook)
'''
