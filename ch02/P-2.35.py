''' P-2.35
Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob’s computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it.
'''

import random
import time


class Alice:
    def __init__(self, probability=0.4):
        self._prob = probability
    
    def create(self):
        ''' creates packet based on thr predefined probability '''
        if self._prob > random.random():
            packet = f'PKG_{round(random.random()*1000)}'
            print(f'-> Alice created a packet \'{packet}\'')
            return packet


class Bob:
    def __init__(self, probability=0.5):
        self._prob = probability
        self._inbox = []
    
    def update(self, new):
        ''' adds received packets to inbox '''
        if new:
            print(f'-> Bob received a packet \'{new}\' from Alice.')
            self._inbox.append(new)
    
    def read(self):
        ''' reads and deletes packets based on the predefined probability
        
        if there is any packets in inbox '''
        if self._prob > random.random() and self._inbox:
            print('-> Bob read the packets from Alice and deleted them.')
            self._inbox.clear()


class InternetProcess:
    def __init__(self, sender, recever):
        self._sender = sender
        self._recever = recever
    
    def _deliver(self, packet):
        self._recever.update(packet)
    
    def run(self, n=10):
        for i in range(n):
            print(f'Time: {i}')
            packet = self._sender.create()
            if packet:
                self._deliver(packet)
            self._recever.read()
            time.sleep(1)  # 1s time delay (optional)


if __name__ == '__main__':
    alice = Alice()
    bob = Bob()
    ip = InternetProcess(alice, bob)
    ip.run()
