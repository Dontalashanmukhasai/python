#Creating a Function
def my_function():
  print("Hello from a function")

#Calling a Function
def my_function():
  print("Hello from a function")

#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Python Function Arguments
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")
evenOdd(2)
evenOdd(3)
