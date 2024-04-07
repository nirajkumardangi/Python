### create a function
def myFunction():
  print("Hello from a function")
### calling a function
myFunction()  


"""
NOTE-1: A parameter is the variable listed inside the parentheses in the function definition.
NOTE-2: An argument is the value that is sent to the function when it is called.
"""
def studentName(names): #parameter
  print(names + " Refsnes")

studentName("Alex") #argument
studentName("John") #argument
studentName("Doe")  #argument


### Number of argument 
def my_function1(fname, lname):
  print(fname + " " + lname)

my_function1("John", "Doe") #John Doe
# my_function1("John")        #error


### Arbitrary Arguments, *args: function will receive a tuple of arguments
def my_function2(*kids):
  print("kids name: {}" .format(kids))
  print("kid1 name: {}" .format(kids[0]))
  print(type(kids))

my_function2("doe", "bob", "mice")  


### Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function3(child1, child2, child3):
  print("The youngest child is " + child1 + " " + child3)

my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Default parameter 
def my_function4(fname, lname="kumar"):
  print("fname: "+ fname, end=" ") 
  print("lname: "+ lname, end=" ")
my_function4("Niraj")