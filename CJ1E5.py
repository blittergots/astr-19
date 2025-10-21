#This is Prompt 5 of Code Journal 1.

import numpy as np

#defining 2 pi into something readable for me
TWO_PI = 2*np.pi

def Make_Big_Table():
	x = 0
	table_text = "|x 	| sin(x) 	|"
	i = 0
	while (i<1000):
		table_text = table_text + "\n|" + str(x) + " 	| " + str(np.sin(x)) + " 	|"
		x = x + TWO_PI/999
		i = i + 1

	print(table_text)

def main():
	Make_Big_Table()

if __name__=="__main__":
	main()