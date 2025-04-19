""" Write a Python program that writes out a table of the function sin(x) vs. x, 
where x is tabulated between 0 and 2 with a thousand entries. 
Follow the basic Python program structure, including a main program function.
"""

import math
import numpy as np

def main():
	x_values = np.linspace(0, 2, 1000)
	# This will generate 1000 values between 0 and 2 that are equally spaced
	print("x\t\tsin(x)")
	print("-" * 20)

	for x in x_values:
			print(f"{x:.6f}\t{math.sin(x):.6f}")

if __name__ == "__main__":
	main()