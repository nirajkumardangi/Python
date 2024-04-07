### Recursion: when a function call itself repeatedly. same as loop, all problem also solved by recursion and vice-versa, in recursion function store in stack memory location.  

# print n to 1 backwards
def show(n):
  if n == 0:
    return
  print(n)
  show(n-1)
  print("END")

# show(3)  


# return n! factorial
def fact(n):
  if(n == 1 or n == 0):
    return 1
  else:
    return n * fact(n-1)

n = 4
print("Factorial of", n, "=", fact(n))
  