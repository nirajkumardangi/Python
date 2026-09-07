# abstraction: hiding implementation details of a class and only showing only essential feature to the user.

from abc import ABC, abstractmethod

class TalkingToy(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def speak(self):
        pass

class RobotToy(TalkingToy):
    def speak(self):
        print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
    def speak(self):
        print(f'{self.name} says ROOOOAR!')

# Toys create karna
rusty = RobotToy('Rusty') # Rusty says beep boop! I am a robot!
fluffy = TeddyBearToy('Fluffy') # Fluffy says hug me! I'm cuddly!
rex = DinosaurToy('Rex') # Rex says ROOOOAR!

toys = [rusty, fluffy, rex]
for toy in toys:
    toy.speak()
    
    
"""---------------------------------------------"""    

class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False

  def start(self):
    self.acc = True
    self.clutch = True
    print("Car Started...")

car1 = Car()
car1.start()