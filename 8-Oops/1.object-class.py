#Objects - Classes - Constructors

#define class
class Student:
  #default constructor
  # def __init__(self):
  #   pass 

  #parameterized constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("adding new student in database...")

s1 = Student("niraj", 21) #object
print(s1.name, s1.age)
