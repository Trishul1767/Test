class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
        self.awake:bool=False
    def greet(self):
        return f'Hello, my name is {self.name}'
    def eat(self):
        if self.awake:
            print(f"{self.name} is awake.")
        else:
            self.awake=True
            print(f"{self.name} just woke up.")
p = Person('John',36)
print(p.greet())

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.awake:bool=False
        self.waking:bool=False
        self.snack:bool=False
    def bark(self):
        print(f'{self.name} says Woof!')
    def wake_up(self):
        if self.awake:
            print("Dog is already awake.")
        else:
            self.awake=True
            print("Dog is now awake.")
    def sleep(self):
        if self.awake:
            self.awake=False
            print("Dog is now asleep.")
        else:
            print("Dog is already asleep.")
    def walk(self):
        if self.walking:
            print("Dog already had a walk today.")
        else:
            self.walking= True
            print("Dog has now went for a walk.")
    def snacks(self):
        if self.snack:
            print("Dog already had snacks today.")
        else:
            print("Dog is now having snacks.")
            self.snack=True
d1=Dog('Buddy',3)
d1.bark()
