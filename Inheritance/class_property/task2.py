# Task 2: Implement a class Rectangle where the width and height attributes use the property decorator 
# to calculate the area and perimeter dynamically when accessed.

class Rectangle:
    def __init__(self, width :float, height:float):
        self.width = width
        self.height = height
        
        
    @property
    def width(self):
        return self.__width
    
    def width(self, value: float)->None:
        if isinstance(value, (int, float)) and value > 0:
            self.__width = value
        else:
            raise ValueError("width must be int/float and greather than Zero...")
        
    
    @property
    def height(self):
        return self.__width
    
    def height(self, value: float)->None:
        if isinstance(value, (int, float)) and value > 0:
            self.__width = value
        else:
            raise ValueError("height must be int/float and greather than Zero...")
        
        
    @property
    def area(self):
        return self.height * self.width
    
    
    
    @property
    def perimetr(self):
        return 2 * (self.height + self.width)
    
    
    def __str__(self):
        return f"({self.width} : {self.height})"
    
    
r1 = Rectangle(20.0,10.0)
print(r1)
print(r1.area)
print(r1.perimetr)
