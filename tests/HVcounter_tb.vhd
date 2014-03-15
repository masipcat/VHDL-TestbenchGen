library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity hvcounter_tb is
end hvcounter_tb;

architecture behav of hvcounter_tb is
	component my_hvcounter
	port (	h : out std_logic_vector (9 downto 0);
			v : out std_logic_vector (9 downto 0);
			clk : in std_logic;
	end component;
	for dut : my_hvcounter use entity work.hvcounter;
	signal t_h : std_logic_vector (9 downto 0);
	signal t_v : std_logic_vector (9 downto 0);
	signal t_clk : std_logic;
begin
	dut: my_hvcounterport map (
		h	=> t_h,
		v	=> t_v,
		clk	=> t_clk);