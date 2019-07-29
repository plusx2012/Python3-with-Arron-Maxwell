class Quarter:
    value = 25
    def in_nickels(self):
        return self.value // 5

quarter = Quarter()
print(quarter.in_nickels() )




class  Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

    def formal_name(self, titlr):
        return title + " " + self.full_name()


person = Person("John", "Smith")

print(person.first)
print(person.last)
