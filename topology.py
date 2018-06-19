from random import randint
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switch = None
        for x in range(randint(0, 10)):
            first = switch
            switch = self.addSwitch('s%s' % (x))
            for h in range(randint(0, 20) + x):
                host = self.addHost('h%s' % (h + 1)*x)
                self.addLink(host, switch)
            if first:
                linkopts = dict(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
                self.addLink(first, switch, linkopts)

topos = { 'mytopo': (lambda: MyTopo()) }
