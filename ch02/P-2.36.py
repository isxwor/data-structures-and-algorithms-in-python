''' P-2.36
Write a Python program to simulate an ecosystem containing two types
of creatures, bears and ﬁsh. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a ﬁsh collide, however, then the
ﬁsh dies (i.e., it disappears).
'''


import random


class Bear:
    def __str__(self):
        return 'B'


class Fish:
    def __str__(self):
        return 'F'


class River:
    def __init__(self, length=20):
        self._length = length
        self._river = []
        for _ in range(length):
            rc = random.choice([Bear(), Fish(), None])
            self._river.append(rc)
        self._processed = set()
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        return self._river[k]
    
    def __setitem__(self, k, val):
        self._river[k] = val
    
    def _empty_cells(self):
        cells = []
        i = 0
        while True:
            try:
                i = self._river.index(None, i)
                cells.append(i)
                i += 1
            except ValueError:
                break
        return cells
    
    def _add_random(self, creature):
        ec = self._empty_cells()
        if ec:
            random_cell = random.choice(ec)
            self[random_cell] = creature
            self._processed.add(random_cell)
    
    def _update_cell(self, index):
        rc = random.randint(0, 2)
        if rc != 0 and self[index] is not None:
            current_creature = self[index]
            i = index-1 if rc == 1 else index+1
            try:
                nxt = self[i]
            except IndexError:
                nxt = self[0]  # circular river system
                i = 0
            if nxt is None:
                self[i] = current_creature
                self[index] = None
            else:
                if type(current_creature) == type(nxt):
                    self._add_random(current_creature)
                else:
                    self[i] = Bear()  # Bear eats Fish
                    if isinstance(current_creature, Fish):
                        i = index
                    self[index] = None
            p = (i if i >= 0 else len(self)-1)
            self._processed.add(p)
    
    def update_river(self):
        for index in range(len(self)):
            if index not in self._processed:
                self._update_cell(index)
        self._processed.clear()  # resets after each cycle
    
    def __str__(self):
        state = ''
        for object in self._river:
            if object is None:
                state += ' -'
            else:
                state += f' {str(object)}'
        return state


if __name__ == '__main__':
    r = River()
    print(f'Initial river:\n{r}')
    for c in range(1, 11):
        r.update_river()
        print(f'\nAfter cycle {c}\n{r}')
