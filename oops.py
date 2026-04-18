class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def greet(self):
        return f'Hello, my name is {self.name}'
p = Person('John',36)
print(p.greet())

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f'{self.name} says Woof!')
d1=Dog('Buddy',3)
d1.bark()