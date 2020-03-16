''' C-2.28
The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge.
'''

class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
    
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number.')
        elif price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be a number.')
        elif amount < 0:
            raise ValueError('Amount cannot be negative.')
        else:
            self._balance -= amount


class PredatoryCreditCard(CreditCard):
    MAX_CHARGES = 10
    
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._charge_count = 0
    
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            self._charge_count += 1
            if self._charge_count > PredatoryCreditCard.MAX_CHARGES:
                self._balance += 1
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
        self._charge_count = 0  # resets at the begining of each month


if __name__ == '__main__':
    wallet = PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 8)
    
    for val in range(15):
        wallet.charge(100)
    
    print(wallet.get_balance())
