import array

class Darray:
    def __init__(self, capacity:int = 1, value:int = 0):
        self.set_cap(capacity)
        self.set_size(0)
        self.__arr = array.array("i", self.__capacity * [value])
        
    def set_size(self, size)-> None:
        if isinstance(size, int) and size >= 0:
            self.__size = size
            
    def set_cap(self,capacity) -> None:
        if isinstance(capacity, int) and capacity >= 0:
            self.__capacity = capacity
            
    def get_size(self) -> int:
        return self.__size
    
    def get_capacity(self) ->int:
        return self.__capacity
        
    def pushback(self, *args)-> None:
        for i in range(len(args)):
            if self.get_capacity() <= self.get_size():
                self.set_cap(self.get_capacity() * 2)
                new_arr = array.array("i", self.get_capacity() * [0])
                for j in range(self.get_size()):
                    new_arr[j] = self.__arr[j]
                self.__arr = new_arr
            self.__arr[self.get_size()] = args[i]
            new_size = self.get_size() + 1
            self.set_size(new_size)
            
                 
    def __str__(self) -> str:
        return f"{[x for x in self.__arr]}"
    
    
a1 = Darray()
print(a1)
a1.pushback(1,2,3,4,5)
print(a1)