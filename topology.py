from random import randint
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switch = None
        magic = randint(5, 10)
        for x in range(randint(0, magic)):
            first = switch
            switch = self.addSwitch('s%s' % (x))
            for h in range(randint(0, 5)):
                host = self.addHost('h%s' % (randint(1, magic*2)))
                self.addLink(host, switch)
            if first:
                linkopts = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
                self.addLink(first, switch, **linkopts)

topos = { 'mytopo': (lambda: MyTopo()) }
