class Pet:
    sound = ""
    def __init__(self,name):
        self.name = name

    def describe(self):
        print("the pet says: {}!".format(self.sound))

    def describe(self):
        kind_of_pet = self.__class__.__name__.lower()
        print("the {} says: {}!".format(kind_of_pet, self.sound))

class Dog(Pet):
    sound = "Woof"

class Cat(Pet):
    sound = "Meow"

class Bird(Pet):
    sound = "Chirp"


rover = Dog("River")
rover.describe()

misty = Cat("Misty")
misty.describe()

angel = Bird("Angel")
angel.describe()

