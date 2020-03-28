''' P-2.37
Write a simulator, as in the previous project, but add a Boolean gender
ﬁeld and a ﬂoating-point strength ﬁeld to each animal, using an Animal
class as a base class. If two animals of the same type try to collide, then
they only create a new instance of that type of animal if they are of different
genders. Otherwise, if two animals of the same type and gender try to
collide, then only the one of larger strength survives.
'''

import random


class Animal:
    def __init__(self):
        self._gender = random.choice('MF')
        self._strength = random.random()


class Bear(Animal):
    def __str__(self):
        return f'B{self._gender}'


class Fish(Animal):
    def __str__(self):
        return f'F{self._gender}'


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
                nxt = self[0]
                i = 0
            if nxt is None:
                self[i] = current_creature
                self[index] = None
            else:
                if type(current_creature) == type(nxt):
                    if current_creature._gender != nxt._gender:
                        self._add_random(current_creature)
                    else:
                        if current_creature._strength > nxt._strength:
                            self[i] = current_creature
                        else:
                            i = index
                        self[index] = None
                else:
                    self[i] = Bear()
                    if isinstance(current_creature, Fish):
                        i = index
                    self[index] = None
            p = (i if i >= 0 else len(self)-1)
            self._processed.add(p)
    
    def update_river(self):
        for index in range(len(self)):
            if index not in self._processed:
                self._update_cell(index)
        self._processed.clear()
    
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
