Documentation
=============


**getLibs():**

Retornara un str con las librerias tal cual, con los saltos de linea y lo que sea necesario

**getEntityTb():**

Retornara una tupla de dos str, uno con el nombre simple de la entidad y otro con el nombre de la entidad que se creará en el tb:
('entidad_tb', 'entidad') 

**getPorts():**

Retornará los puertos tal cual:
   port( a, b, c_in : in  std_logic;
         s, c_out   : out std_logic); 

**getPortSignal():**

Agrupará los puertos y los meterá en un diccionarios, la key sera el tipo de puerto (std_logic, std_logic_vector(3 downto 0)...) y los valores serán una lista con
los puertos:

{'std_logic':['a', 'b', 'c_in', 's', 'c_out'], 'std_logic_vector(5 downto 0)': ['etc']} 
