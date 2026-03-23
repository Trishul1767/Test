class Car:
    def __init__(self,model:str,horsepower:int):
        self.model=model
        self.horsepower=horsepower
        self.turn_on_engine:bool=False
    
    def turn_on(self):
        if self.turn_on_engine:
            print(f'{self.model} engine is already on')
        else:
            self.turn_on_engine=True
            print(f'{self.model} engine is now on')
     
    def turn_off(self):
        if self.turn_on_engine:
            self.turn_on_engine=False
            print(f'{self.model} engine is now off')
        else:
            print(f'{self.model} engine is already off')

    def run_lap(self,lap:int):
        if self.turn_on_engine:
            print(f'{self.model} completes {lap} lap(s) with {self.horsepower} horsepower')
        else:
            print(f'{self.model} engine is off. Please turn it on to run laps.')

    def __str__(self):
        return f'Car(model = {self.model}, horsepower = {self.horsepower})'
    
    def __repr__(self):
        return f'Car(model = {self.model}, horsepower = {self.horsepower})'

x=Car('Nexon',118)
y=Car('Harrier',140)
z=Car('m340i',250)
print(str(x))
z.turn_on()
z.run_lap(3)
z.turn_off()





