class Person:
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    def full_name(self):
        return "{} {} {}".format(self.first, self.middle,  self.last)

    def formal_name(self, title):
        return "{} {}".format(title, self.full_name())



person = Person("Cosmin", "Ioan", "Streza")
print(person.full_name())
print(person.formal_name("Mr."))

