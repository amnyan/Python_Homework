class Person:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.msg = f"{self.name} got grade {self.grade}"
        
    def show(self):
        return f"{self.name} got grade {self.grade}"
        
        
p1 = Person("Arman", 99)
p1.name = "Hasmik"
p1.grade = 80
print(p1.msg)
print(p1.show())