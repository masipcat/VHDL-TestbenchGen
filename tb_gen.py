#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from vhdl import *
sys.argv += ["hex7seg.vhd"]

if len(sys.argv) != 2:
	sys.exit(1)

# Nom del fitxer vhdl
vhd_file = sys.argv[1]

def read_file(filename):
	f = open(filename, "r")
	content = f.read()
	f.close()
	return content

def getBetween(s, pref, suf):
	try:
		start = s.index(pref) # if start != 0 else 0
		end = s[start:].index(suf)
		return (s[start + len(pref):start+end], start+end)
	except Exception:
		return ("", -1)

def getEntities(vhdl_file):
	entities = []
	value = ("", 0)
	while True:
		value = getBetween(vhd[value[1]:], "entity ", " is")
		if value != ("", -1) and Entity(value[0]) not in entities:
			ent_content = getBetween(vhdl_file, value[0] + " is", "end " + value[0] + ";")
			print ent_content
			entities += [Entity(value[0])]
		else:
			break
	return entities

def getLibs(vhd_file):
	pass

lib = Library("IEEE")
lib.addPackage("std_logic")

vhd = read_file(vhd_file).lower()
file = VHDL()
file.setEntities(getEntities(vhd))
file.addLibrary(lib)
print file