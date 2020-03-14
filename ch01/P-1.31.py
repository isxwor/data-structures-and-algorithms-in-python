''' P-1.31
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
'''

# -- Based on Nepal government's monetary system --
def make_change(charge, given):
    BILLS_COINS = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    change = {}
    changeDue = round(given - charge)
    return_amount = changeDue
    for val in BILLS_COINS:
        amount, changeDue = divmod(changeDue, val)
        if amount: # adds only non zero values
            change[val] = int(amount)
    return return_amount, change


if __name__ == '__main__':
    while True:
        charge = int(input('Enter chargeable amount: '))
        given = int(input('Enter given amount: '))
        if charge > given:
            print('Insufficient amount!')
        else:
            r = make_change(charge, given)
            break
    print('Bills and Coins to return')
    for key, val in r[1].items():
        if int(key) == 1:
            print(f'-- {val}x Re{key}')
        else:
            print(f'-- {val}x Rs{key}')
    print(f'Amount to be returned: Rs {r[0]}')
