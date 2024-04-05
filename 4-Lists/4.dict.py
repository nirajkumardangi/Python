# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionaries items are key-value pairs that are separated by commas and enclosed within curly brackets {}. changeable and do not allow duplicates.

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(dict1)        
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'colors': ['red', 'white', 'blue']}

print(dict1["brand"])     # Ford
print(dict1.get("model")) # Mustang
print(dict1.keys())       # dict_keys(['brand', 'model', 'year', 'colors'])
print(dict1.values())     # dict_values(['Ford', 'Mustang', 2020, ['red', 'white', 'blue']])
dict1["seater"] = "five"  # adding items
print(dict1)

dict1.pop("colors") # removing items
print(dict1)

for x in dict1:     # loop dict
  print(x)          # Print all key names
  print(dict1[x])   # Print all value names

for x, y in dict1.items():  
  print(x, y)       # both keys and values


# Nested Dictionary: -------------------------------------------------------------
myFamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}  
print(myFamily)


#------------------------------------------------------------------------------

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myFamily1 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myFamily1)