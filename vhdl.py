#!/usr/bin/python
# -*- coding: utf-8 -*-

class VHDL(object):

	def __init__(self):
		self._libs = []
		self._entities = []

	def setEntities(self, ents):
		if isinstance(ents, list):
			self._entities = ents

	def getEntities(self):
		return self._entities

	def addLibrary(self, lib):
		if isinstance(lib, Library):
			if lib not in self._libs:
				self._libs += [lib]
				return True
		return False

	def removeLibrary(self, lib):
		try:
			self._libs.remove(lib)
			return True
		except Exception:
			return False

	def __str__(self):
		return "\n".join([str(l) for l in self._libs])

class Library(object):

	def __init__(self, value):
		self._lib = value
		self._packages = []

	def addPackage(self, package_name):
		self._packages += [self._lib + "." + package_name]

	def getName(self):
		return self._lib

	def __eq__(self, other):
		if isinstance(other, Library):
			return self._lib == other.getName()
		return False

	def __str__(self):
		return "library " + self._lib + ";" + "".join(["\nuse " + p + ";" for p in self._packages])

class Entity(object):

	def __init__(self, name):
		self._name = name
		self._port = ""#[]

	def getName(self):
		return self._name

	def setPort(self, p):
		#if isinstance(p, Port):
		#self._port += [p]
		self._port = p
		return True
		#return False

	def getPorts(self):
		return self._port

	def __str__(self):
		return "<Entity " + self._name + ">"

	def __eq__(self, other):
		return self._name == other.getName() if isinstance(other, Entity) else False

class Signal(object):

	_obj_name = "signal"
	_name = ""
	_type = ""

	def __init__(self, name, type):
		self.setName(name)
		self.setType(type)

	def getName(self):
		return self._name

	def setName(self, n):
		if isinstance(n, str):
			self._name = n
		else:
			print "ERR: " + self._obj_name + " name must be a string"

	def getType(self):
		return self._type

	def setType(self, t):
		if isinstance(t, str):
			self._type = t
		else:
			print "ERR: " + self._obj_name + " type must be a string"

	def __str__(self):
		return "<" + self._obj_name.capitalize() + " " + self._name + " : " + self._type + ">"

	def __eq__(self, other):
		if isinstance(other, Signal):
			return self._name == other.getName() and self._type == other.getType()
		return False

class PortList(object):

	def __init__(self, port_str):
		pass

class Port(Signal):

	_obj_name = "port"
	_port_type = "in"

	def __init__(self, name, port_type, type):
		Signal.__init__(self, name, type)
		self.setPortType(port_type)

	def setPortType(self, t):
		if t in ["in", "out", "inout", "buffer", "linkage"]:
			self._port_type = t
		else:
			print "ERR: '" + str(t) + "' isn't a valid port_type for", self._obj_name + " '" + self._name + "'. "

	def getPortType(self):
		return self._port_type

	def __str__(self):
		return "<" + self._obj_name.capitalize() + " " + self._name + " : " + self._port_type + " " + self._type + ">"

	def __eq__(self, other):
		if isinstance(other, Port):
			return self._name == other.getName() and self._type == other.getType() and self._port_type == other.getPortType()
		return False

class Architecture(object):

	_begin = ""
	_name = ""
	_archOf = None

	def __init__(self, name, ent):
		if isinstance(name, str):
			self._name = name
		else:
			print "architecture hasn't a valid name"
		if isinstance(ent, Entity):
			self._archOf = ent
		else:
			print self._name, "architecture hasn't a valid entity"

	def setBegin(self, b):
		self._begin = b

	def getBegin(self):
		return self._begin

	def getEntity(self):
		return self._archOf

	def __str__(self):
		return "<Architecture " + self._name + " of " + self._archOf.getName() + ">"