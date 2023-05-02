from string import ascii_lowercase

def compare_cats(cat):
    return 42
class Animal:

    pass

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def __gt__(self, other): # LESS THAN <
        return self.name < other.name

cats = [Cat(c) for c in ascii_lowercase]
cats.sort()

print(Cat("Z") > Cat("A"))
