class Pixel:
    def __init__(self, x :int = 0, y:int = 0):
        self.set_x(x)
        self.set_y(y)
        
    def set_x(self,x : int) -> None:
        if isinstance(x, int) or isinstance(x, float):
            self.__x = x
            
    def set_y(self, y : int) -> None:
        if isinstance(y,int) or isinstance(y, float):
            self.__y = y
            
    def get_y(self) -> int:
        return self.__y  
    
    def get_x(self) -> int:
        return self.__x 
    
    
    def __repr__(self) :
        return f"Pixel({self.get_x()}, {self.get_y()})"
    
#     def __str__(self):
#         return f"""
# X -> {self.get_x()}
# Y -> {self.get_y()}          
#     """
    def __add__(self,other : 'Pixel') -> 'Pixel':
        return Pixel(self.get_x() + other.get_x(), self.get_y() + other.get_y())
    
    def __sub__(self,other : 'Pixel') -> 'Pixel':
        return Pixel(self.get_x() - other.get_x(), self.get_y() - other.get_y())
    
    def __mul__(self,other : 'Pixel') -> 'Pixel':
        return Pixel(self.get_x() * other.get_x(), self.get_y() * other.get_y())
    
    def __truediv__(self,other : 'Pixel') -> 'Pixel':
        if other.get_x() == 0 or other.get_y() == 0:
            raise ValueError("Cann't divide to Zero...")
        return Pixel(self.get_x() / other.get_x(), self.get_y() / other.get_y())
    
    def __eq__(self, other:'Pixel') -> True:
        return True if self.get_x() == other.get_x() and self.get_y() == other.get_y() else False
    
    def __lt__(self, other: 'Pixel') -> True:
       return True if self.get_x() < other.get_x() and self.get_y() < other.get_y() else False 
   
    def __le__(self, other: 'Pixel') -> True:
       return True if self.get_x() <= other.get_x() and self.get_y() <= other.get_y() else False 
   
    def __gt__(self, other: 'Pixel') -> True:
       return True if self.get_x() > other.get_x() and self.get_y() > other.get_y() else False 
   
    def __ge__(self, other: 'Pixel') -> True:
       return True if self.get_x() >= other.get_x() and self.get_y() >= other.get_y() else False 
   
    def __ne__(self, other:'Pixel') -> True:
        return True if self.get_x() != other.get_x() and self.get_y() != other.get_y() else False
    
    def __bool__(self) -> bool:
        return True
    
    def __hash__(self) -> int:
        return hash((self.get_x(), self.get_y()))


pixels = [Pixel(x,y) for (x,y) in zip(range(0,32,2), range(1,32,2))]
# [print(x) for x in pixels]
# [print(f"{x} + {y} = {x + y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} - {y} = {x - y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} * {y} = {x * y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} / {y} = {x / y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} === {y} = {x == y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} < {y} = {x < y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} <= {y} = {x <= y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} > {y} = {x > y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} <= {y} = {x <= y}") for (x,y) in zip(pixels[:8], pixels[8:])]
# [print(f"{x} != {y} = {x != y}") for (x,y) in zip(pixels[:8], pixels[8:])]
[print(hash(x)) for x in pixels]

mydict= {
    "name" : "Arman",
    pixels[0] : "pixel"
}

print(mydict)
