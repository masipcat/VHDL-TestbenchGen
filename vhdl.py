#!/usr/bin/python
# -*- coding: utf-8 -*-

class VHDL(object):

	def __init__(self):
		self._libs = []
		self._entities = {}
		self._archs = {}

	def setEntity(self, ent):
		if isinstance(ent, Entity):
			self._entities[ent.getName()] = ent

	def getEntities(self):
		return self._entities.values()

	def getEntityByName(self, ent_name):
		if ent_name in self._entities.keys():
			return self._entities[ent_name]
		return False

	def setArchitecture(self, arch):
		if isinstance(arch, Architecture):
			self._archs[arch.getName()] = arch

	def getArchitectures(self):
		return self._archs.values()

	def getArchitectureByName(self, arch_name):
		if arch_name in self._arch.keys():
			return self._arch[arch_name]
		return False

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
		self._port = {}

	def getName(self):
		return self._name

	def setPortList(self, p):
		if isinstance(p, PortList):
			self._port = p.getPorts()
			return True
		return False

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

class PortList(object):

	def __init__(self, port_str):
		self._ports = self._getPortFromString(port_str.strip())

	def getPorts(self):
		return self._ports

	def _getPortFromString(self, s):
		ports = {}
		counting = False
		bracket_count = 0
		between_port = ""
		skip_times = 0
		for i in range(len(s)):
			if skip_times > 0:
				skip_times -= 1
				continue
			if s[i:i+4] == "port":
				counting = True
				skip_times = 3
				continue
			elif s[i] == "(":
				bracket_count += 1
			elif s[i] == ")":
				bracket_count -= 1
				if bracket_count == 0:
					break
			if counting:
				between_port += s[i]
		port = ""
		for line in between_port.strip()[1:].strip().split("\n"):
			port += line.strip()
		try:
			for p in port.split(";"):
				port_name, type = p.split(":")
				port_name = port_name.strip()
				type = type.strip()
				for i in range(len(type)):
					if type[i] == " ":
						port_type = type[:i]
						variable_type = type[i+1:]
						break
				if "," in port_name:
					for n in port_name.split(","):
						n = n.strip()
						ports[n] = Port(n, port_type, variable_type)
				else:		
					ports[port_name] = Port(port_name, port_type, variable_type)
		except Exception as e:
			print "ERR: Cannot read port from string:", e
		return ports

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

	def getName(self):
		return self._name

	def getEntity(self):
		return self._archOf

	def setBegin(self, b):
		self._begin = b

	def getBegin(self):
		return self._begin

	def getEntity(self):
		return self._archOf

	def __str__(self):
		return "<Architecture " + self._name + " of " + self._archOf.getName() + ">"