
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs} legs")

    def return_legs(self):
        return self._number_of_legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)

class Dog(Animal):
    def __init__(self,legs_count, name):
        super().__init__(legs_count)
        self._name = name
    
    def get_name(self):
        return self._name
    
    def bark(self):
        print('woof woof')
        
d = Dog(4,'Rex')
print(f'the name of dog d is {d.get_name()}')
d.bark()
d.count_legs()
    