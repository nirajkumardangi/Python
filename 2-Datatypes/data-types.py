# Number Data Types: int, float, complex ################################################
num1 = 10; # integer
print(num1 , "is type of" , type(num1)) 

num2 = 10.10 #float
print(num2 , "is type of" , type(num2))

num3 = 5 + 10j #complex
print(num3 , "is type of" , type(num3))


# String Types: ################################################
name = 'Python'
print(name)  

message = "Python for beginners"
print(message)


# Sequence Types: list, tuple, range ################################################
# -> sequence store multiple data together in a single variable.

# List (list): Lists are ordered collections of items enclosed within square brackets [ ]. Lists can contain elements of different data types and are mutable, meaning their elements can be changed after creation. For example: [1, 2, 3], ['a', 'b', 'c'], [1, 'hello', True].
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [1, 'hello', True]
print(list1 , "is type of" , type(list1))

list2.append('x')
print(list2)


# Tuple (tuple): Tuples are similar to lists, but they are immutable, meaning their elements cannot be changed after creation. Tuples are defined using parentheses ( ). For example: (1, 2, 3), ('a', 'b', 'c'), (1, 'hello', True).
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'hello', True)
print(tuple1 , "is type of" , type(tuple1))

tuple2.append('hlo') #error: can't append because tuple are immutable
print(tuple2)


# Dictionary (dict): Dictionaries are unordered collections of key-value pairs enclosed within curly braces { }. Each key-value pair maps the key to its corresponding value. Dictionaries are mutable. For example: {'name': 'John', 'age': 30, 'city': 'New York'}.
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
print(dict1 , "is type of" , type(dict1))


# Set (set): Sets are unordered collections of unique elements enclosed within curly braces { }. Sets do not allow duplicate elements. For example: {1, 2, 3}, {'a', 'b', 'c'}.

set1 =  {1, 2, 2, 2, 2, 3}, {'a', 'b', 'c'}
print(set1, "is type of" , type(set1))