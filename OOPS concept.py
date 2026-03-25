class Car:
    def __init__(self,model:str,horsepower:int):
        self.model=model
        self.horsepower=horsepower
        self.turn_on_engine:bool=False
        self.fuel_gauge:float=100.0
    
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
            if self.fuel_gauge>=lap*5:
                print(f'{self.model} completes {lap} lap(s) with {self.horsepower} horsepower')
                self.fuel_gauge-=lap*5
                print(f'{self.model} fuel gauge: {self.fuel_gauge}%')
            else:
                print(f'{self.model} does not have enough fuel to complete {lap} lap(s).')
        else:
            print(f'{self.model} engine is off. Please turn it on to run laps.')

    def __str__(self):
        return f'Car(model = {self.model}, horsepower = {self.horsepower})'
    
    def __repr__(self):
        return f'Car(model = {self.model}, horsepower = {self.horsepower})'
    def fuel_up(self,x:float):
        self.fuel_gauge=x
        print(f'{self.model} fuel gauge is now full.')

x=Car('Nexon',118)
y=Car('Harrier',140)
z=Car('m340i',250)
print(repr(x))
z.turn_on()
z.run_lap(3)
#z.fuel_up()
z.run_lap(10)
z.run_lap(7)
z.fuel_up(500)
z.run_lap(1)
z.turn_off()


