library ieee; 
use ieee.std_logic_1164.all;

entity full_adder is
   port( a, b, c_in : in  std_logic;
         s, c_out   : out std_logic);
end full_adder;

architecture arch_1 of full_adder is
   signal temp : std_logic;
begin
   temp  <= a xor b;
   s     <= temp xor c_in;
   c_out <= (a and b) or (c_in and temp);
end;
