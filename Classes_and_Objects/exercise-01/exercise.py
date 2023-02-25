class Animal():
    def __init__(self, legs):
        self.leg_count = legs
    
        
    def runs(self):
        print("Running started")
        
a = Animal(4)

print("Animal object was created")     

a.runs()