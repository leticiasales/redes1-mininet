from random import randint
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switch = None
        for x in range(randint(0, 10)):
            first = switch
            switch = self.addSwitch('s%s' % (x))
            for h in range(randint(0, 20)):
                host = self.addHost('h%s' % (h + 1))
                self.addLink(host, switch)
            if first:
                self.addLink(first, switch)

topos = { 'mytopo': (lambda: MyTopo()) }
