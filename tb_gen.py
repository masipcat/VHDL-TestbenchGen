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
vhd_file = read_file(vhd_file).lower()

# Create a new VHDL object
vhdl = VHDL()

# Add libraries and packages to 'vhdl'
for l in getLibs(vhd_file):
	vhdl.addLibrary(l)

# Add entities to 'vhdl'
for entity in getEntities(vhd_file):
	vhdl.setEntity(entity)

# Get each entity in 'vhdl' and adds each architecture in 'vhdl'
for entity in vhdl.getEntities():
	arch = getArchitectureOfEntity(vhd_file, entity)
	if arch != "":
		vhdl.setArchitecture(arch)

# ---------------------------
# AQUÍ VA EL CÓDIGO DE FELIPE
# ---------------------------

# Get each arch in vhdl file
for architecture in vhdl.getArchitectures():
	print architecture

	# Get each signal in arch
	for signal in architecture.getSignalList().values():
		print "\t", signal
	
	# Get the entity of arch
	entity = architecture.getEntity()
	print "\t", entity

	# Print each port defined in entity statment
	for port in entity.getPorts().values():
		print "\t\t", port