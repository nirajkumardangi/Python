# Sets are unordered collection of data items. They store multiple items in a single variable. Sets items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

info = {"Carla", 19, False, 5.9, 19}
print(info)  # {False, 'Carla', 19, 5.9}


# Access Items : ---------------------------------------------------------------
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop.

set1 = {"apple", "banana", "mango"}
for x in set1:
  print(x)

print("apple" in set1)  # True 


# Add Set Items: Once a set is created, you cannot change its items, but you can add new items.
# add(): add items to the set.
fruits = {"mango", "apple"}
fruits.add("orange")
print(fruits)  # {'apple', 'orange', 'mango'}

# update(): add items from another set into the current set
fruits1 = {"mango", "apple"}
vegetables = {"onion", "potato"}
fruits1.update(vegetables)
print(fruits1)  # {'onion', 'apple', 'potato', 'mango'}


# Remove Set Items: -------------------------------------------------------------

# remove(): remove an items in a set.
# NOTE: If the item to remove does not exist, remove() will raise an error.
fruits2 = {"mango", "apple", "banana"}
fruits2.remove("mango")
print(fruits2)  # {'apple', 'banana'}


# discard(): remove an items in a set. 
# NOTE: If the item to remove does not exist, discard() will NOT raise an error.
fruits3 = {"mango", "apple", "banana"}
fruits3.discard("apple")
print(fruits3)  # {'banana', 'mango'}


# pop(): random item, because it is an unordered collection of items.
fruits4 = {"mango", "apple", "banana"}
fruits4.pop()
print(fruits4)


# clear(): empty the set
fruits5 = {"mango", "apple", "banana"}
fruits5.clear()
print(fruits5)  # set()


# Loop Items: ------------------------------------------------------------------
fruits6 = {"apple", "banana", "cherry"}

for x in fruits6:
  print(x)


# Set Methods: -----------------------------------------------------------------
"""
add()	          : Adds an element to the set
clear()	        : Removes all the elements from the set
copy()	        : Returns a copy of the set
difference()	  : Returns a set containing the difference between two or more sets
difference_update() : Removes the items in this set that are also included in another, specified set
discard()	      : Remove the specified item
intersection()	: Returns a set, that is the intersection of two other sets
intersection_update() :	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	  : Returns whether two sets have a intersection or not
issubset()	    : Returns whether another set contains this set or not
issuperset()  	: Returns whether this set contains another set or not
pop()	          : Removes an element from the set
remove()	      : Removes the specified element
symmetric_difference() : Returns a set with the symmetric differences of two sets
symmetric_difference_update() :	inserts the symmetric differences from this set and another
union()	        : Return a set containing the union of sets
update()	      : Update the set with the union of this set and others

"""