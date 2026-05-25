#encapsulation with setter and getter method
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
emp = Employee("John Doe", 50000)
print(emp.get_name())  # Output: John Doe
print(emp.get_salary())  # Output: 50000
emp.set_name("Jane Doe")
emp.set_salary(60000)
print(emp.get_name())  # Output: Jane Doe
print(emp.get_salary())  # Output: 60000



#Encapsulation with only setter method
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary
emp = Employee("John Doe", 50000)
emp.set_name("Jane Doe")
emp.set_salary(60000)
print(emp._Employee__name)  # Output: Jane Doe
print(emp._Employee__salary)  # Output: 60000


#Encapsulation with only getter method
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary
emp = Employee("John Doe", 50000)
print(emp.get_name())  # Output: John Doe
print(emp.get_salary())  # Output: 50000

