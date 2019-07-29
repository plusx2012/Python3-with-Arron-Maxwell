'''

Imagine writing a game called Orcs Vs. Goblins. You will, of course,
need goblins:

>>> goby = Goblin('Goby')
>>> goby.name
'Goby'

>>> goby.hitpoints
10
>>> goby.damage
3

You'll also need orcs, who are a bit bigger and tougher:

>>> morgash = Orc('Morgash')
>>> morgash.name
'Morgash'
>>> morgash.hitpoints
15
>>> morgash.damage
5

You can check whether a creature is alive:

>>> morgash.is_alive()
True
>>> morgash.hitpoints = 0
>>> morgash.is_alive()
False
>>> morgash.hitpoints = 10
>>> morgash.is_alive()
True

Both goblins and orcs inherit from a class called Critter.
IMPORTANT: Put as many methods and member variables as possible in
this base class. Can you find a way to put ALL the methods in Critter?

>>> isinstance(goby, Critter)
True
>>> isinstance(morgash, Critter)
True

This being a fighting game, critters can (and will) attack each other.
(Notice the attack() method returns the amount of damage done.)

>>> goby.hitpoints
10
>>> morgash.hitpoints
10
>>> morgash.attack(goby)
5
>>> goby.hitpoints
5
>>> goby.attack(morgash)
3
>>> goby.attack(morgash)
3
>>> morgash.hitpoints
4

Hit points can't go below zero, though:
>>> goby.attack(morgash)
3
>>> morgash.hitpoints
1
>>> goby.attack(morgash)
1
>>> morgash.hitpoints
0
>>> goby.attack(morgash)
0
>>> morgash.hitpoints
0

Critters can describe themselves, which we'll use in the user interface:

>>> goby.describe()
'Goby the Goblin'
>>> morgash.describe()
'Morgash the Orc'

'''

# Write your code here:

class Critter:
    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return self.hitpoints > 0

    def attack(self, target):
        damage = self.damage
        if damage > target.hitpoints:
            damage = target.hitpoints
        target.hitpoints -= damage
        return damage

    def describe(self):
        return f'{self.name} the {self.__class__.__name__}'

class Goblin(Critter):
    hitpoints = 10
    damage = 3

class Orc(Critter):
    hitpoints = 15
    damage = 5

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
