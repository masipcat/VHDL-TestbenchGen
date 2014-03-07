LIBRARY ieee ;
use ieee.std_logic_1164.all;

entity hex7seg is
	port ( entrada : in std_logic_vector (7 downto 0);
			a ,b ,c ,d ,e ,f , g : out std_logic );
end hex7seg;

architecture arc of hex7seg is
	signal bus_out : std_logic_vector (6 downto 0);
begin
	with entrada select
		bus_out <= 	"1111110" when x"45",
					"0110000" when x"16",
					"1101101" when x"1E",
					"1001111" when x"26",
					"0110011" when x"25",
					"1011011" when x"2E",
					"1011111" when x"36",
					"1110000" when x"3D",
					"1111111" when x"3E",
					"1111011" when x"46",
					"1110111" when x"1C",
					"0011111" when x"32",
					"1001110" when x"21",
					"0111101" when x"23",
					"1001111" when x"24",
					"1000111" when x"2B",
					"-------" when others;
			(a ,b ,c ,d ,e ,f , g ) <= bus_out;
end arc;
