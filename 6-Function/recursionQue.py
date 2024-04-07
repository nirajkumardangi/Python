# Q1. Calculate factorial?
def fact(n):
  if(n == 1 or n ==0):
    return 1
  else:
    return n * fact(n-1)

n = 3
print("The factorial of", n, "=", fact(n))


# Q2. Countdown to zero.
def countdown(t):
  if t == 0:
    print("Blast off!")
  else:
    print(t)
    countdown(t - 1)
  
countdown(5)


# Q3. Fibonacci sequence.
def fibonacci(n):
  if n < 0:
    raise ValueError("n must be non-negative integer")
  elif n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n - 2)
# calculate the first 10 fibonacci number
for i in range(8):
  print(fibonacci(i))  
    

# Q4. Calculate the sum of first n natural number
def calcSum(n):
  if n <= 1:
    return n
  else:
    return n + calcSum(n-1)

print(calcSum(5))



