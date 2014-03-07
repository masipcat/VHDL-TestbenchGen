List of 

**getLibs():**
Retornara un str con las librerías tal cual, con los saltos de linea y lo que sea necesario

**ObtenirentitatTb():**
Retornara una tupla de dos str, uno con el nombre simple de la entidad y otro con el nombre de la entidad que se creará en el tb:
('entidad_tb', 'entidad') 

**getPorts():**
Retornará los puertos tal cual:
   port( a, b, c_in : in  std_logic;
         s, c_out   : out std_logic); 

**getSignal():**
Retornará un str con la palabra 'signal' al incio y los puertos añadiendo 't_' al inicio de su nombre, separados por coma y al final de estos, el tipo de los puertos y el punto y coma: signal t_a , t_b , t_c_in, t_s , t_c_out : std_logic ;