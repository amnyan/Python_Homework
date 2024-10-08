class Person:
    __slots__ = ("__name", "__age", "__email")
    
    def __init__(self, name:str, age:int, email:str):
        self.name = name
        self.age = age
        self.email = email
        
        
    @property
    def name(self)-> str:
        return self.__name
    
    
    @name.setter
    def name(self,value:str)-> None:
        if isinstance(value, str) and value != "":
            self.__name = value
        else:
            raise ValueError("name must be not empty")
    
    
    @property
    def age(self)->int:
        return self.__age
    
    @age.setter
    def age(self,value:str)-> None:
        if isinstance(value, int) and value > 0:
            self.__age = value
        else:
            raise ValueError("age must be positive")
    
    
    @property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email(self,value:str)-> None:
        if isinstance(value, str) and value != "" and value.endswith("@gmail.com"):
            self.__email = value
        else:
            raise ValueError("email must be ends with '@gmail.com'")
    
    def __str__(self)->str:
        return f" {self.name} - {self.age} - {self.email}"
    

p1 = Person("Arman",1,"arman@gmail.com")



    
    