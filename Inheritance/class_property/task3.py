# Task 3: Write a class Temperature that stores temperature in Celsius
# but allows the user to set and get the temperature in Fahrenheit using the property decorator.


class Temperature:
    def __init__(self,celsius:float):
        self.celsius = celsius
        
        
    @property
    def celsius(self)->float:
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value:float) -> None:
        if isinstance(value, (int, float)):
            self.__celsius = value
        else:
            raise ValueError("Celsius must be integer or float...")
        
    @property    
    def fahrenheit(self)->float:
        return (self.celsius * 9 / 5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value:float)->None:
        if isinstance(value, (int, float)):
            self.celsius = (value - 32) * 5 / 9
        else:
            raise ValueError("Celsius must be integer or float...")
        
        
    def __str__(self):
        return f"Temperature {self.celsius}C({self.fahrenheit}F)"
        
        
        
t1 = Temperature(10)
# t1.fahrenheit = 10
t1.celsius= 100
# t1.fahrenheit = 100
print(t1)
        
    