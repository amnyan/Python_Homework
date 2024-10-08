from typing import Any
class DynamicArray:
    def __init__(self, capacity: int = 10):
        self.set_capacity(capacity)
        
        
    def set_capacity(self, capacity: int):
        if isinstance(capacity, int):
            self.__capacity = capacity
            
            
    def __getitem__(self, index: int) -> Any:
        return self[index]