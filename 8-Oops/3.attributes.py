class Student:
  college_name = "Ranchi University" #only one time store in memory
  name = "anonymous" #class attributes
  
  def __init__(self, name, age):
    self.name = name  #obj attr > class attr
    self.age = age
    print("adding new student in database...")

s1 = Student("niraj", 21)
print(s1.name)
