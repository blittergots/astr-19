#This program is prompt 3 of Code Journal #1.

#defining a function that returns x**3 + 8.
def f(x): 
	return x**3+8

def main():
	x=9
	result=f(x)
	print(result)
	if result > 27:
		print ("yay!")

if __name__=="__main__":
	main()
