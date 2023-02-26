
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")
        
    def nb_of_legs(self):
        return self.number_of_legs
    
a = Animal(4)
print(f'a animal has {a.number_of_legs} legs')

