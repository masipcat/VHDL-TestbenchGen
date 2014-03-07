#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from vhdl import *
from magic_methods import *

# Used to test code using SublimeText
sys.argv += ["tests/hex7seg.vhd"]

if len(sys.argv) != 2:
	print "Filename not specified"
	sys.exit(1)

# Get VHDL file from arguments
vhd_file = sys.argv[1]

# Read VHDL file
vhd = read_file(vhd_file).lower()

# Create a new VHDL object
file = VHDL()

# Add entities to file
file.setEntities(getEntities(vhd))

# Test code
for l in getLibs(vhd):
	file.addLibrary(l)
for entity in file.getEntities():
	print entity.getPorts()