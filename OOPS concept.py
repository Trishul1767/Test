# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")
class Car:
    def __init__(self,model:str,horsepower:int):
        self.__model=model
        self.horsepower=horsepower
        self.turn_on_engine:bool=False
        self.fuel_gauge:float=100.0
        self.laps_R:int=8
    
    def turn_on(self):
        if self.turn_on_engine:
            print(f'{self.__model} engine is already on')
        else:
            self.turn_on_engine=True
            print(f'{self.__model} engine is now on')
     
    def turn_off(self):
        if self.turn_on_engine:
            self.turn_on_engine=False
            print(f'{self.__model} engine is now off')
        else:
            print(f'{self.__model} engine is already off')

    def run_lap(self,lap:int):
        if self.turn_on_engine:
            if self.laps_R>=lap:
                if self.fuel_gauge>=lap*5:
                    self.fuel_gauge-=lap*5
                    self.laps_R-=lap
                    print(f'{self.__model} completes {lap} lap(s). Fuel gauge: {self.fuel_gauge}%')
                else:
                    print(f'{self.__model} does not have enough fuel to complete {lap} lap(s).')
            else:
                print(f"There are only {self.laps_R} laps remaining")
        else:
            print(f'{self.__model} engine is off. Please turn it on to run laps.')

    def __str__(self):
        return f'Car(model = {self.__model}, horsepower = {self.horsepower})'
    
    def __repr__(self):
        return f'Car(model = {self.__model}, horsepower = {self.horsepower})'
    
    def fuel_up(self,x:float):
        self.fuel_gauge+=x
        print(f'{self.__model} fuel gauge is now full.')
    
    def check_fuel(self):
        print(f'{self.__model} fuel gauge: {self.fuel_gauge}%')

    def laps_remaining(self):
        print(f"Number of laps remained are {self.laps_R}")
        
    def setter(self,name):
        self.__model=name
        
    def getter(self):
        return self.__model

z=Car('m340i',250)
z.turn_on()
z.run_lap(10)
z.run_lap(5)
z.laps_remaining()
z.check_fuel()
z.run_lap(2)
z.setter('i20')
print(z.getter())
z.setter('m3')
print(z.getter())





