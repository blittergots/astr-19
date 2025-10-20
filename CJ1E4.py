#This is prompt 4 of Code Journal #1.

#Defining a class that describes my favorite animal

#here are all of the parameters for the class
class Favorite_Animal:
	def __init__(self, arms, legs, eyes, tail, furry):
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

#this prints out the info on the animal
	def describe(self):
		print(f"wingspan: {self.arms}")
		print(f"leg length: {self.legs}")
		print(f"number of eyes: {self.eyes}")
		print(f"tail: {self.tail}")
		print(f"furry?: {self.furry}")

def main():
	American_Woodcock = Favorite_Animal(16.5, "short and stocky", "two", "short and fluffy", "feathery")
	American_Woodcock.describe()

if __name__=="__main__":
	main()