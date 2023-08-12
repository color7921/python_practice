class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age) 

class Employee(Person):
    def __init__(self, name, age, ID):
        super().init(name, age)
        self.ID = ID
    def getID(self):
        return self.ID
    