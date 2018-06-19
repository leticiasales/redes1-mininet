from random import random
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self, n = 4):
        Topo.__init__(self)
        first = null
        for x in random.random:
            first = switch
            switch = self.addSwitch('s%s' % (x))
            for h in range(n):
                host = self.addHost('h%s' % (h + 1))
                self.addLink(host, switch)
            if first != null
                self.addLink(first, switch)

topos = { 'mytopo': (lambda: MyTopo()) }
