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

# Add libraries and packages to 'file'
for l in getLibs(vhd):
	file.addLibrary(l)

# Add entities to file
for entity in getEntities(vhd):
	file.setEntity(entity)

# Get each entity in 'file' and adds each architecture in 'file'
for entity in file.getEntities():
	arch = getArchitecture(vhd, entity)
	if arch != "":
		file.setArchitecture(arch)

# ----------------------------
# AQUÍ VA EL CÓDIGO DEL FELIPE
# ----------------------------

for architecture in file.getArchitectures():
	print architecture
	entity = architecture.getEntity()
	print "\t", entity
	print "\t\t", entity.getPorts()