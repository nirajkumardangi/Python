class Cat:
    def speak(self):
        return "A cat meow"

class Bird:
    def speak(self):
        return "A bird tweet"

class Monkey:
    def speak(self):
        return "A monkey ooh ooh aah aah ooh ooh aah aah"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat()) # A cat meow
animal_sound(Bird()) # A bird tweet
animal_sound(Monkey()) # A monkey ooh ooh aah aah ooh ooh aah aah


"""
Inheritance-Based Polymorphism
"""

class Animal:
    def speak(self):
        return 'Some generic sound'

class Cat(Animal):
    def speak(self):
        return 'A cat meow'

class Dog(Animal):
    def speak(self):
        return 'A dog barks woof woof'

class Monkey(Animal):
    def speak(self):
        return 'A monkey ooh ooh aah aah ooh ooh aah aah'

print(Cat().speak())     # A cat meow
print(Dog().speak())     # A dog barks woof woof
print(Monkey().speak())  # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak())  # Some generic sound
