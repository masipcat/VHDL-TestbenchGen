#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from vhdl import *
from vParser import *

name=sys.argv[1]


if len(sys.argv) != 2:
	print "Especifica nom del fitxer"
	sys.exit(1)


if '.vhd' not in name:
	print 'Extenció no vàlida'
	sys.exit(1)


maketb=name.split('.')
maketb=maketb[0]+'_tb.'+maketb[1]
tb_result = ""

vhd_file = sys.argv[1]

vhd_file = read_file(vhd_file).lower()

vhdl = VHDL()

for l in getLibs(vhd_file):
	vhdl.addLibrary(l)

for entity in getEntities(vhd_file):
	vhdl.setEntity(entity)

# Get each entity in 'vhdl' and adds each architecture in 'vhdl'
for entity in vhdl.getEntities():
	arch = getArchitectureOfEntity(vhd_file, entity)
	if arch != "":
		vhdl.setArchitecture(arch)


print """
dP     dP dP     dP  888888ba  dP        
88     88 88     88  88    `8b 88        
88    .8P 88aaaaa88a 88     88 88        
88    d8' 88     88  88     88 88        
88  .d8P  88     88  88    .8P 88        
888888'   dP     dP  8888888P  88888888P 
ooooooooooooooooooooooooooooooooooooooooo
                                         
d888888P  888888ba   .88888.                    
   88     88    `8b d8'   `88                   
   88    a88aaaa8P' 88        .d8888b. 88d888b. 
   88     88   `8b. 88   YP88 88ooood8 88'  `88 
   88     88    .88 Y8.   .88 88.  ... 88    88 
   dP     88888888P  `88888'  `88888P' dP    dP 
oooooooooooooooooooooooooooooooooooooooooooooooo

version: 1.0
author: Felipe Arango, Jordi Masip

"""

	
def LibrarysTb(): #Librerias
	result = ""
	libss=[]
	use=[]
	for lib in vhdl.getLibs():
		result += 'library '+lib.getName()+';\n'
	
	for lib in vhdl.getLibs():
		for pack in lib.getPackages(): 
			result += "use " + pack+';\n'
	return result + "\n"
			
def entityTb(): #Entidad
	result = ""
	for architecture in vhdl.getArchitectures():
		entity = architecture.getEntity()		#Puede ser global?
		result += 'entity '+entity.getName()+'_tb is'+'\n'+'end '+entity.getName()+'_tb;\n'
	return result + "\n"

def architectureTb():
	result = ""
	for architecture in vhdl.getArchitectures():
		entity = architecture.getEntity()
	result += 'architecture behav of '+entity.getName()+'_tb is\n'+'\tcomponent my_'+entity.getName()+'\n'
	return result

def portsTb():
	result = '\tport ('
	for architecture in vhdl.getArchitectures():
		entity = architecture.getEntity()
		for i, port in enumerate(entity.getPorts().values()):
			if i != 0:
				result += '\t\t'
			result += '\t'+port.getName()+' : '+port.getPortType()+' '+port.getType()+';\n'
			if i == len(entity.getPorts().values())-1:
				result = result[:-2] + ");\n"
		result += '\tend component;'
	return result

def dutSignalsTb():
	result = ""
	for architecture in vhdl.getArchitectures():
		entity = architecture.getEntity()
		result += '\n\tfor dut : my_'+entity.getName()+' use entity work.'+entity.getName()+';\n'
		for port in entity.getPorts().values():
			result += '\tsignal t_'+port.getName()+' : '+port.getType()+';\n'
		result += 'begin\n'
	return result
		
def dutTb():
	result = ""
	b=0
	for architecture in vhdl.getArchitectures():
		entity = architecture.getEntity()
		result += '\tdut: my_'+entity.getName()+' port map (\n'
		for port in entity.getPorts().values():
			if b != len(entity.getPorts().values())-1:
				result += '\t\t'+port.getName()+'\t=> t_'+port.getName()+',\n'
				b+=1
			else:
				result += '\t\t'+port.getName()+'\t=> t_'+port.getName()+');\n'
	return result

def clocktb():
	result=""
	res='sn'
	while True: 
		clk = raw_input('Vols un clock?: [s/n]')
		if clk != 's' and clk != 'n':
			print clk
			print 'Opció no vàlida'
		elif clk == 's':
			result+="\tclk_process: process\n\tbegin\n\t\tt_clk <= '0';\n\t\twait for ¿? ns;\n\t\tfor i in 1 to ¿? loop\n\t\t\tt_clk <= not t_clk;\n\t\t\twait for ¿? ns;\n\t\tend loop;\n\t\twait;\n\t end process clk_process;"
			return result
		else:
			return result
			
tb_result += LibrarysTb()
tb_result += entityTb()
tb_result += architectureTb()
tb_result += portsTb()
tb_result += dutSignalsTb()
tb_result += dutTb()
tb_result += clocktb()

# Write to file
write_file(maketb, tb_result)
print maketb+' creat'
