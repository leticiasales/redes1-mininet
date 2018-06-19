from random import choice
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switch = None
        max_labs = 4
        for x in range(labs):
            lab[x] = self.addSwitch('s%s' % (x))
            for h in range(20 - ((x > 2)? x * 5 : 0)):
                host = self.addHost('h%s-lab%s' % (h), (x))
                self.addLink(host, switch)
            if first:
                self.addLink(first, switch, bw=randint(5, 10))

topos = { 'mytopo': (lambda: MyTopo()) }
