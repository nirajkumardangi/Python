# string data types
my_string = "niraj";
print(my_string)


# multiline string
multiline_string = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''';
print(multiline_string)


# string are array
a = 'my name is niraj';
print("string are array: "+ a[0]);


# looping trough a string
for x in "banana":
  print(x);


# string length
a = 'my name is niraj';
print("Length : "+ str(len(a)))


# checking string
text = "how are you manish"
print("are" in text)
print("is" in text) 


#########################################################################################

# slicing string
greet = "Good Morning!"
print(greet[0:5])  # from - to
print(greet[:5])  # from the start 
print(greet[0:])  # to the end  


#########################################################################################

# modify string
greet1 = "Namaste, Hello India";
print(greet1.upper())  #uppercase
print(greet1.lower())  #lowercase
print(greet1.replace("Namaste", "Hello"))  #replace
print(greet1.split(","))
print(greet1)


#########################################################################################

# concat string
a1 = "hello"
b1 = "world"
print(a1 + b1)


#########################################################################################

# formate method 
quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

my_order1 = "I want {2} pieces of item {0} for {1} dollars."
print(my_order1.format(quantity, item_no, price))


#########################################################################################

# All string methods

""" 
capitalize() : Converts the first character to upper case
count() : Returns the number of times a specified value occurs in a string
find() : Searches the string for a specified value and returns the position of where it was found
format() : Formats specified values in a string
format_map() : Formats specified values in a string
index() : Searches the string for a specified value and returns the position of where it was found
isalnum() : Returns True if all characters in the string are alphanumeric
isalpha() : Returns True if all characters in the string are in the alphabet
isascii() : Returns True if all characters in the string are ascii characters
isdecimal() : Returns True if all characters in the string are decimals
isdigit() : Returns True if all characters in the string are digits
isidentifier() : Returns True if the string is an identifier
islower() : Returns True if all characters in the string are lower case
isnumeric() : Returns True if all characters in the string are numeric
isprintable() : Returns True if all characters in the string are printable
isspace() : Returns True if all characters in the string are whitespaces
istitle() : Returns True if the string follows the rules of a title
isupper() : Returns True if all characters in the string are upper case
join() : Joins the elements of an iterable to the end of the string
ljust() : Returns a left justified version of the string
lower() : Converts a string into lower case
lstrip() : Returns a left trim version of the string
maketrans() : Returns a translation table to be used in translations
partition() : Returns a tuple where the string is parted into three parts
replace() : Returns a string where a specified value is replaced with a specified value
rfind() : Searches the string for a specified value and returns the last position of where it was found
rindex() : Searches the string for a specified value and returns the last position of where it was found
rjust() : Returns a right justified version of the string
rpartition() : Returns a tuple where the string is parted into three parts
rsplit() : Splits the string at the specified separator, and returns a list
rstrip() : Returns a right trim version of the string
split() : Splits the string at the specified separator, and returns a list
splitlines() : Splits the string at line breaks and returns a list
startswith() : Returns true if the string starts with the specified value
strip() : Returns a trimmed version of the string
swapcase() : Swaps cases, lower case becomes upper case and vice versa
title() : Converts the first character of each word to upper case
translate() : Returns a translated string
upper() : Converts a string into upper case
zfill() : Fills the string with a specified number of 0 values at the beginning 

"""