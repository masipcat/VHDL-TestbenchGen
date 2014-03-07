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
		start = s.index(pref) # if start != 0 else 0
		end = s[start:].index(suf)
		return (s[start + len(pref):start+end], start+end)
	except Exception:
		return ("", -1)

def getEntities(vhdl_file):
	entities = []
	value = ("", 0)
	while True:
		value = getBetween(vhdl_file[value[1]:], "entity ", " is")
		if value != ("", -1) and Entity(value[0]) not in entities:
			ent_content = getBetween(vhdl_file, value[0] + " is", "end " + value[0] + ";")
			between_entity = ent_content[0].strip()
			invalid_port = True
			port = ""
			count = 0
			counting = False
			for i, char in enumerate(between_entity):
				if char == "p":
					if between_entity[i:4] == "port":
						counting = True
				if counting:
					port += char
					if char == "(":
						count += 1
					elif char == ")":
						count -= 1
						if between_entity[i+1] == ";" and count == 0:
							port += ";"
							invalid_port = False
							break
			else:
				invalid_port = True
			ent = Entity(value[0])
			if not invalid_port:
				#ent.setPortList(port)
				ent.setPort(port)
			entities += [ent]
		else:
			break
	return entities

def getLibs(vhdl_file):
	libs = {}
	value = ("", 0)
	i = 0
	while True:
		value = getBetween(vhdl_file[value[1]:], "library", ";")
		if value[1] == -1:
			break
		lib_name = value[0].strip().lower()
		libs[lib_name] = Library(lib_name)
	value = ("", 0)
	while True:
		value = getBetween(vhdl_file[value[1]:], "use", ";")
		if value[1] == -1:
			break
		use_statment = value[0].strip().lower().split(".")
		lib, package = use_statment[0], ".".join(use_statment[1:])
		if lib in libs.keys():
			libs[lib].addPackage(package)
	return libs.values()