''' P-1.35
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people ﬁnd it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,... ,100.
'''


from random import randint
from datetime import datetime, timedelta


def random_birthdays(n):
    base = datetime(2020, 1, 1) # first day of the year
    return [base + timedelta(days=randint(0, 365)) for _ in range(n)]

def probability(n, tests=100):  # running 100 tests to get an average of
    total_match = 0             # how often there is a match in n no. of people
    for _ in range(tests):
        birthdays = random_birthdays(n)
        match = set(x for x in birthdays if birthdays.count(x) > 1)
        if len(match) >= 1:
            total_match += 1
    return total_match/tests * 100


if __name__ == '__main__':
    for n in range(5, 105, 5):
        result = probability(n)
        print(f'{result:.1f}% probability in {n} people.')
