library ieee;
use ieee.std_logic_1164.all;

entity full_adder_tb is
end full_adder_tb ;

architecture behav of full_adder_tb is
   component my_adder
   port ( a, b, c_in : in std_logic ;
           s, c_out  : out std_logic);
   end component ;
   for dut : my_adder use entity work.full_adder ;
signal t_a , t_b , t_c_in, t_s , t_c_out : std_logic ;
begin
-- Component instantiation . 
dut : my_adder port map ( a     => t_a ,
                          b     => t_b ,
                          c_in  => t_c_in ,
                          s     => t_s ,
                          c_out => t_c_out );

  process
     begin
     t_a    <= '0';
     t_b    <= '0';
     t_c_in <= '0';
     wait for 1 sec;
     t_a    <= '0';
     t_b    <= '1';
     t_c_in <= '0';
     wait for 1 sec; 
     wait;
  end process ;
end behav;