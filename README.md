# redes 1 - projeto - mininet

Mininet is a prototyping software for networks. 
 Where you can create custom topologies, switches and SDN controllers.
 You can also set many variables and run simulations.
It has a command line interface where you can run the tests.

sudo mn --switch ovs --controller ref --topo tree,depth=2,fanout=8 --test pingall

- sudo mn: run mininet as root
- --switch ovs: set openvswitch as switch
- --controller ref:
- --topo tree,depth=2,fanout=8: set topology 'tree' with depth 2 and fanout 8
- --test pingall: set test enviroment 'pingall' where all hosts try to ping all hosts. 
The result is displayed on screen.

