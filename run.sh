#!/bin/bash

clear

echo "Iniciando"

test=$1

sudo mn --mac --custom ~/redes/topology.py --topo mytopo --test $1
