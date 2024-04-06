# else if : ------------------------------------------------- 
if 5 > 10:
  print("b is greater than a")
elif 10 == 5:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short Hand of if ------------------------------------------
if 10 > 5 : print("10 is Greater") 


# Short hand of else...if -----------------------------------
print("A") if 10 > 5 else print("B")


# Nested if ------------------------------------------------- 
number = -1
# outer if statement
if number >= 0:
  # inner if statement
  if number == 0:
    print("Number is Zero")
  # inner else statement
  else: 
    print("Number is Positive")
# outer else statement    
else: 
  print("Number is Negative")      