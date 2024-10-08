class Partial:
    def __init__(self, fn, *args):
        self.__fn = fn
        self.__args = args
        
    def __call__(self, *args):
        return self.__fn(*self.__args, * args)
    
    
    
    
def add(a, b, c):
    return a + b + c


p1 = Partial(add, 10)
print(p1(4,6))