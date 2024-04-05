# Tuple : ordered collection of item which is unchangeable means immutable. Allows duplicate members.
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
print(type(tuple1))


# Unpack Tuples: --------------------------------------------------------------- 
fruits1 = ("apple", "banana", "cherry")
(green, yellow, red) = fruits1
print(green)
print(yellow)
print(red)
# Output:: 
"""
apple
banana
cherry
"""

# Use *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# Output:: 
"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""


# Changing Tuples Value: ------------------------------------------------------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "orange"
x = tuple(y)
print(x)  # Output:: ('apple', 'orange', 'cherry')

# Append in Tuple
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")     #add item 
temp.pop(3)               #remove item
temp[2] = "Finland"       #change item
countries = tuple(temp)
print(countries)          # Output:: ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')


# Joining Tuples: -------------------------------------------------------------
tuple3 = ("a", "b" , "c")
tuple4 = (1, 2, 3)
join1 = tuple3 + tuple4
print(join1)  # Output:: ('a', 'b', 'c', 1, 2, 3)


# Multiply Tuples: ------------------------------------------------------------
fruits5 = ("apple", "banana", "cherry")
myTuples = fruits5 * 2
print(myTuples)  # Output:: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')