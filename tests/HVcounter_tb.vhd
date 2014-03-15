library ieee ;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity HVcounter_tb is
end HVcounter_tb ;

architecture counter of HVcounter_tb is
	component my_HVcounter
	port ( 	clk: in STD_LOGIC;
		H  : out STD_LOGIC_VECTOR (9 downto 0);
		V  : out STD_LOGIC_VECTOR (9 downto 0));
 	end component;

 for dut : my_HVcounter use entity work.HVcounter;
 signal clk	: STD_LOGIC:='1';
 signal H	: STD_LOGIC_VECTOR (9 downto 0);
 signal V	: STD_LOGIC_VECTOR (9 downto 0);

begin
 dut: my_HVcounter port map(
	clk	=> clk,
	H	=> H,
	V	=> V);

 clk_process: process
 begin 
	clk <= '1';
	wait for 5 ns;
	for i in 1 to 10000 loop
		clk <= not clk;
		wait for 5 ns;
	end loop;
	wait;
 end process clk_process;
end counter;
