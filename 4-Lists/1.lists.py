# List: ordered collection of item which is changeable means mutable. Allows duplicate members.
thisList1 = [1, "mango", True, 12.2, 10, 20, 30]


# Access List Items -------------------------------------------------------------
print(thisList1[0]) # Output:: 1
print(thisList1[1]) # Output:: mango  
print(thisList1[-1]) # Output:: 30
print(thisList1[0:3]) # Output:: [1, 'mango', True]
print(thisList1[:2]) # Output:: [1, 'mango']


# Change List Items -------------------------------------------------------------
thisList2 = ["apple", "banana", "cherry"]
thisList2[1] = "blackcurrant"
print(thisList2) # Output:: ['apple', 'blackcurrant', 'cherry']

# Change the second and third value by replacing it with one value
thisList2[1:3] = ["blackcurrant", "watermelon"]
print(thisList2) # Output:: ['apple', 'blackcurrant', 'watermelon']

# insert a new list item, without replacing
thisList2.insert(2, "watermelon-2") 
print(thisList2) # Output:: ['apple', 'blackcurrant', 'watermelon-2', 'watermelon']


# Add List Items: ---------------------------------------------------------------
# append(): add an item to the end of the list.
thisList3 = ["apple", "banana", "cherry"]
thisList3.append("orange")
print(thisList3) # Output:: ['apple', 'banana', 'cherry', 'orange']

# insert(): insert a list item at a specified index.
thisList3.insert(1, "orange")
print(thisList3) # Output:: ['apple', 'orange', 'banana', 'cherry', 'orange']

# extend(): append elements from another list to the current list.
thisList3 = ["apple", "banana", "cherry"]
thisList4 = ["mango", "pineapple", "papaya"]
thisList3.extend(thisList4)
print(thisList3) # Output:: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# add any iterable
thisList3 = ["apple", "banana", "cherry"]
thisList4 = ("mango", "pineapple", "papaya")
thisList3.extend(thisList4)
print(thisList3) # Output:: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# Remove List Items -------------------------------------------------------------
thisList5 = ["apple", "banana", "cherry", "banana", "kiwi"]
thisList5.remove("banana")
print(thisList5) # Output:: ['apple', 'cherry', 'banana', 'kiwi']  # removes first occurrence of banana

# pop(1): remove specific item
# pop(): remove last item
thisList6 = ["apple", "banana", "cherry"]
thisList6.pop(1)
thisList6.pop()
print(thisList6) # Output:: ['apple']  # removes banana and cherry

# clear(): empties the list.
thisList7 = ["apple", "banana", "cherry", "banana", "kiwi"]
thisList7.clear()
print(thisList7) # Output:: []  # removes all items from the list


# Loop List --------------------------------------------------------------------
thisList8 = ["apple", "banana", "cherry", "banana", "kiwi"]
for x in thisList8:
  print(x)

for i in range(len(thisList8)):
  print(thisList8[i])


# Sort List --------------------------------------------------------------------
# sort(): Sort the list alphabetically and numerically.
thisList9 = ["orange", "apple", "kiwi", "pineapple", "banana"]
thisList9.sort()
print(thisList9) # Output:: ['apple', 'banana', 'kiwi', 'orange', 'pineapple']

thisList10 = [20, 100, 3, 50]
thisList10.sort()
print(thisList10) # Output:: [3, 20, 50, 100]

# sort(reverse = true): sort descending
thisList11 = [20, 100, 3, 50]
thisList11.sort(reverse=True)
print(thisList11) # Output:: [100, 50, 20, 3]

# reverse(): reverse the order of the list items
thisList12 = ["banana", "Orange", "Kiwi", "cherry"]
thisList12.reverse()
print(thisList12) # Output:: ['cherry', 'Kiwi', 'Orange', 'banana']


# Copy List: --------------------------------------------------------------------
thisList12 = ["banana", "Orange", "Kiwi", "cherry"]
thisList13 = thisList12.copy()
thisList14 = list(thisList12) 
print(thisList12) # Output:: ['banana', 'Orange', 'Kiwi', 'cherry']
print(thisList13) # Output:: ['banana', 'Orange', 'Kiwi', 'cherry']
print(thisList14) # Output:: ['banana', 'Orange', 'Kiwi', 'cherry']


# List Comprehension: -----------------------------------------------------------
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O) # Output:: ['Milo', 'Bruno', 'Rosa']


"""
append()	:  Adds an element at the end of the list
clear()	  :  Removes all the elements from the list
copy()	  :  Returns a copy of the list
count()	  :  Returns the number of elements with the specified value
extend()	:  Add the elements of a list (or any iterable), to the end of the current list
index()	  :  Returns the index of the first element with the specified value
insert()	:  Adds an element at the specified position
pop()	    :  Removes the element at the specified position
remove()	:  Removes the item with the specified value
reverse()	:  Reverses the order of the list
sort()	  :  Sorts the list

"""