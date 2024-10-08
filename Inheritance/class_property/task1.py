# Task 1: Create a class Person that uses the property decorator 
# to control access to the age attribute. Ensure that the age is a positive integer, 
# and if an invalid value is assigned, raise a ValueError.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and  name != "":
            self.__name = name
        else:
            raise ValueError("Name must be String and not empty")
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and  value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be int and greather than 0")

    def __str__(self):
        return f"{self.name} : {self.age}"


p1 = Person("Arman",22)   
p1.name = "Narek"
# p1.age = 1

p1.name = "Harut"
p1._Person__age = -4
print(p1)
# print(p1.__dict__)
# print(Person.__dict__)
    
    