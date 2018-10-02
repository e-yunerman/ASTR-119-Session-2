#include the Numpy library
import numpy as np

#define the main() function
def main():

	i = 0 		#declare integer i, set to 0
	x = 119.0	#declare a float x, with val 119
	
	for i in range(120):	#loops i from 0 to 119
		if((i%2)==0):		#if i is even
			x += 3			#add 3 to x
		else:				#if i is odd
			x -= 5			#subtracts 5 from x
	
	s = "%3.2e" %x			#make a string that shows x with scientific notation
	
	print(s)
	
#now the rest of the program

if __name__ == "__main__":		#this runs the main function
	main()
	
#continue

			