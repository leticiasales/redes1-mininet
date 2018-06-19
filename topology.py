from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
	
		Topo.__init__(self)
		n = 4
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)
        switch = self.addSwitch('s2')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1 + n))
            self.addLink(host, switch)

topos = { 'mytopo': (lambda: MyTopo()) }
