# variables -----------------------------------------------------------
name = "Tony Stark"
age = 25.5
genius = True

print(name)
print(age) 
print(genius)


# castings ------------------------------------------------------------
name = str("Tony Stark")
age = int(28.5)
ageX = float(28.0) 
genius = bool(True)
print(name, age, ageX, genius); # Tony Stark 28 28.0 True


# get the type --------------------------------------------------------
print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(ageX)) # <class 'float'>
print(type(genius)) # <class 'bool'>


# single or double quotes? --------------------------------------------
x = "hello"
#same as 
y = 'hello'


# case sensitive ------------------------------------------------------
a = 4
A = "Sally"
#A will not overwrite a 

name = "Bob"
age = 25
print("Name: {}, Age: {}" .format(name, age))


# Many value to multiple variables ------------------------------------
x, y, z = 'apple', 'banana', 'mango'
print(x, y, z) # output: apple banana mango

# one value to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Many value to multiple variables ------------------------------------


