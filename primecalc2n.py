## The function below outputs the last prime number from a range of numbers from a given input at the command line
## it accepts one argument:
## "nxdnum" for the value of the given index number of the prime that one would like returned
## This script considers 2 to be the first prime number.

## example usage to get the tenth prime number:
## 	python primecalc2n.py 10
## would result in returning 29

def primcalc(endnum, nthnum):
	lst = []
	index = 0
	endnum = endnum * nthnum #increasing endnum, so it is not too small
	for y in range(2, endnum):
		for x in range(2, y):
			if y%x == 0:
				break
		else:
			lst.append(y)
			index = index + 1
			if index == nthnum:
				lastnum = lst[-1]
				break
	return(lastnum)


import sys
try:	
	from sys import argv
	ndxnum = int(argv[1]) 	#input index from command line arg.
	mynum = 10		#setting range to a default of 10, this could be changed to be excepted as an input arg	
	
	f1 = primcalc(mynum, ndxnum) # Calling the function and setting the last value to the input arg from the command line
	print(f1)	# Using this to display the final output of the function to the screen
except IndexError:
	print("Input parameters must be specified, meaning the integer of the prime you are looking for, 1 or greater.")
	sys.exit(1)
except ValueError:
	print("Improper Value Entered, please input integers only, 1 or greater")
	sys.exit(1)
except UnboundLocalError:
	print("The index number specified is out of range! There are no primes in that range, \n please use integers only, 1 or greater.")
sys.exit(1)
