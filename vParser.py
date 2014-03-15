#!/usr/bin/python
# -*- coding: utf-8 -*-

from vhdl import *

def read_file(filename):
	try:
		f = open(filename, "r")
		content = f.read()
		f.close()
		return content
	except Exception as e:
		print "ERR: We couldn't read '%s'" % filename
		return ""

def write_file(filename, content):
	try:
		f = open(filename, "w")
		f.write(content)
		f.close()
	except Exception as e:
		print "ERR: We couldn't write '%s'" % filename

def getBetween(s, pref, suf):
	try:
		start = 0 if pref == "" else s.index(pref)
		end = len(s) if suf == "" else s[start:].index(suf)
		return (s[start + len(pref):start+end], end)
	except Exception:
		return ("", -1)

def getLibs(vhdl_file):
	libs = {}
	if "library" not in vhdl_file:
		return []
	last_pos = 0
	while True:
		value = getBetween(vhdl_file[last_pos:], "library", ";")
		last_pos += value[1]
		if value == ("", -1):
			break
		lib_name = value[0].strip().lower()
		if lib_name in libs:
			break
		libs[lib_name] = Library(lib_name)
	last_pos = 0
	while True:
		value = getBetween(vhdl_file[last_pos:], "use", ";")
		last_pos += value[1]
		if value == ("", -1):
			break
		use_statment = value[0].strip().lower().split(".")
		lib, package = use_statment[0], ".".join(use_statment[1:])
		if lib in libs.keys():
			libs[lib].addPackage(package)
		else:
			print "ERR: Using library '%s' in package '%s.%s' without adding the library" % (lib, lib, package)
			break
	return libs.values()

def getEntities(vhdl_file):
	entities = []
	last_pos = 0
	while True:
		value = getBetween(vhdl_file[last_pos:], "entity", "is")
		entity = Entity(value[0].strip())
		if value == ("", -1) or entity in entities:
			break
		last_pos += value[1]
		between_entity = getBetween(vhdl_file, entity.getName() + " is", "end")[0].strip()
		port = ""
		bracket_counter = 0
		isCounting, isPortFound, isValidPort = False, False, False
		for i in range(len(between_entity)):
			if between_entity[i:i+4] == "port":
				isCounting = True
				isPortFound = True
			if isCounting:
				port += between_entity[i]
				if between_entity[i] == "(":
					bracket_counter += 1
				elif between_entity[i] == ")":
					bracket_counter -= 1
				elif between_entity[i] == ";" and bracket_counter == 0:
					isPortFound = True
					isValidPort = True
					break
		else:
			isValidPort = False

		if isValidPort:
			entity.setPortList(PortList(port))
		elif isPortFound:
			print "ERR: Cannot read port defined in '%s' entity" % entity.getName()
		entities += [entity]
	return entities

def getArchitectureOfEntity(vhdl_file, entity):
	last_pos = 0
	while True:
		value = getBetween(vhdl_file[last_pos:], "architecture", "begin")
		last_pos += value[1]
		arch_name = getBetween(value[0], "", " of")[0].strip()
		ent_name = getBetween(value[0], "of ", "is")[0].strip()
		if arch_name == "" or ent_name == "":
			break
		if ent_name != entity.getName():
			continue
		arch = Architecture(arch_name, entity)
		signals = getBetween(value[0], "is", "")[0].strip()
		if signals != "":
			arch.setSignalList(SignalList(signals))
		return arch