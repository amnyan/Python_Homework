# Task 4: Implement a Descriptor class to manage access to a score attribute in a Student class. 
# Use the __get__ and __set__ methods to ensure the score is within a valid range (e.g., 0-100).

class ScoreDescriptor:
    def __init__(self):
        self.__score = None
    
    def __set__(self,instance,  value:int)->None:
        if isinstance(value, int) and value > 0 and value < 100:
            self.__score = value
        else:
            raise ValueError("Score must be integer and (0-100)")
        
    def __get__(self,instance, owner)->int:
        return self.__score
    
    
    
class Student:
    score = ScoreDescriptor()
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __str__(self):
        return f"Student: {self.name}, Score: {self.score}"
    
    
    
s1 = Student("Arman",99)

# s1.score = 190
print(s1)