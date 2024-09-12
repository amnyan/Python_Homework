# Write a Python class named Person that has attributes for name and age. Include a method to display the person’s details.

class Person:
    def __init__(self, name : str, age : int):
        self.__set_name(name)
        self.__set_age(age)
    def __set_name(self, name : str) -> None:
        if isinstance(name, str):
            self.__name = name
        else :
            self.__name = None
            
    def __get_name(self)-> str:
        return self.__name
    
    def __set_age(self,age:int)-> None:
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            self.__age = None 
            
    def __get_age(self) -> int:
        return self.__age
    
    def display(self):
        print(f"Name is {self.__get_name()} and age is {self.__get_age()}")
        

p1 = Person("Arman", 10)
p1.display()