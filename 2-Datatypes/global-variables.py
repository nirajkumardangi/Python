# global variable ###########################################################

x = 'awesome'
def myFunction():
  x = 'hello'
  print(x)

myFunction()

print(x)


# global keyword ###########################################################

def myfun():
  global a
  a = 'good'
  print(a)

myfun()
print(a)




