from random import choice
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switch = None
        max_labs = 4
        lab = [0,0,0,0]
        for x in range(labs):
            lab[x] = self.addSwitch('s%s' % (x))
            for h in range(20 - (5 and (x > 2) or 0) * 5):
                host = self.addHost('h%s-lab%s' % (h), (x))
                self.addLink(host, switch)
            if first:
                self.addLink(first, switch, bw=randint(5, 10))

topos = { 'mytopo': (lambda: MyTopo()) }
