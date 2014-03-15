library ieee ;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity HVcounter is 
	port ( 	clk: in STD_LOGIC;
		H  : out STD_LOGIC_VECTOR (9 downto 0);
        V  : out STD_LOGIC_VECTOR (9 downto 0));
end HVcounter;

architecture counter of HVcounter is 
	signal q: unsigned(9 downto 0):="0000000000";
	signal w: unsigned(9 downto 0):="0000000000";
	
begin
	process(clk)
	begin
		if rising_edge(clk) then
			if q = 799 then 
				q <= "0000000000";
				w <= w + 1;
			
			elsif w /= 0 and w <= 524 then
				w <= w + 1;
				q <= q + 1;
				
			else
				w <= "0000000000"; 
				q <= q + 1;

			end if;
		end if;
	end process;
	H <= STD_LOGIC_VECTOR(q);
	V <= STD_LOGIC_VECTOR(w);
end counter;	

    
