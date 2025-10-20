#this program is prompt 2 of Code Journal 1.

#the sum of 2 floating point numbers
def add_two_floats():
	x=89.3
	y=4.99
	sum=x+y
	print(sum)
	print(type(sum))

#the difference between two integers
def subtract_two_integers():
	difference = 5 - 4
	print(difference)
	print(type(difference))

#multiplying a function
def multiply_float_integer():
	x=4
	y=4.8
	product=x*y
	print(product)
	print(type(product))

def main():
	add_two_floats()
	subtract_two_integers()
	multiply_float_integer()

if __name__=="__main__":
	main()