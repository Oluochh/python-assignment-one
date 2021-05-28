class Dog:
        def __init__(self,color,weight,age):
            self.color=color
            self.weight=weight
            self.age=age
        def bark(self):
             return f"The {self.color} dog with {self.weight} has passed on with{self.age} years "
        def  attack(self):
            return f"The {self.color} dog attacked the {self.age} puppy which was only {self.weight} kg"  