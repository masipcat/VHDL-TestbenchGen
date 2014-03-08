#!/usr/bin/python
# -*- coding: utf-8 -*-

from vhdl import *

def read_file(filename):
	f = open(filename, "r")
	content = f.read()
	f.close()
	return content

def getBetween(s, pref, suf):
	try:
		if pref == "":
			start = 0
		else:
			start = s.index(pref) # if start != 0 else 0
		if suf == "":
			end = len(s)
		else:
			end = s[start:].index(suf)
		return (s[start + len(pref):start+end], start+end)
	except Exception:
		return ("", -1)

def getLibs(vhdl_file):
	libs = {}
	value = ("", 0)
	while True:
		value = getBetween(vhdl_file[value[1]:], "library", ";")
		if value[1] == -1:
			break
		lib_name = value[0].strip().lower()
		libs[lib_name] = Library(lib_name)
	value = ("", 0)
	while True:
		value = getBetween(vhdl_file[value[1]:], "use", ";")
		if value == ("", -1):
			break
		use_statment = value[0].strip().lower().split(".")
		lib, package = use_statment[0], ".".join(use_statment[1:])
		if lib in libs.keys():
			libs[lib].addPackage(package)
		else:
			print "ERR: Using library '" + lib + "' in package '" + lib + "." + package + ";' without adding the library"
			break
	return libs.values()

def getEntities(vhdl_file):
	entities = []
	value = ("", 0)
	while True:
		value = getBetween(vhdl_file[value[1]:], "entity", "is")
		entity = Entity(value[0].strip())
		if value == ("", -1) or entity in entities:
			break
		between_entity = getBetween(vhdl_file, entity.getName() + " is", "end")[0].strip()
		port = ""
		bracket_counter = 0
		isCounting, isPortFound = False, False
		for i in range(len(between_entity)):
			if between_entity[i:i+4] == "port":
				isCounting = True
			if isCounting:
				port += between_entity[i]
				if between_entity[i] == "(":
					bracket_counter += 1
				elif between_entity[i] == ")" or between_entity[i:i+1] == ");":
					bracket_counter -= 1
					if bracket_counter == 0:
						port += ";"
						isPortFound = True
						break
		else:
			isPortFound = False
		
		if isPortFound:
			entity.setPortList(PortList(port))
		entities += [entity]
	return entities

def getArchitectureOfEntity(vhdl_file, entity):
	value = ("", 0)
	while True:
		value = getBetween(vhdl_file[value[1]:], "architecture ", " is")
		arch_name = getBetween(value[0], "", " of")[0].strip()
		ent_name = getBetween(value[0], "of ", "")[0].strip()
		if arch_name == "" or ent_name == "":
			break
		if ent_name != entity.getName():
			continue
		arch = Architecture(arch_name, entity)
		signals = getBetween(vhdl_file[value[1]:], "is", "begin")[0].strip()
		if signals != "":
			arch.setSignalList(SignalList(signals))
		return arch