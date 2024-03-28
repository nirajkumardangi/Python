# when a function written in class is called method
class Student:
  college_name = "Ranchi University"
  
  def __init__(self, name, age):
    self.name = name  #obj attr > class attr
    self.age = age

  def greet(self):
    print("Good Morning!", self.name)

s1 = Student("niraj", 21)
s1.greet()


# static method: method that don't use self parameter (work at class level) 
class Greeting:
  @staticmethod
  def greet():
    print("Hello Mrs...")

g1 = Greeting()
g1.greet()