# Design a class Employee with private attributes employee_id, name, and salary. Provide methods to set and get these values. Ensure that salary cannot be negative.

class Employee:
    def __init__(self,employee_id, name : str, salary : int) -> None:
        self.set_employee_id(employee_id)
        self.set_name(name)
        self.set_salary(salary)
    
    def set_employee_id(self, id : int) -> None:
        if isinstance(id, int) and id > 0:
            self.__employee_id = id
        else:
            self.__employee_id = None
            
    def set_name(self, name : str) -> None:
        if isinstance(name, str) and len(name) >= 3:
            self.__name = name
        else:
            self.__name = None
            
    def set_salary(self, salary : int) -> None:
        if isinstance(salary, int) and salary > 0:
            self.__salary = salary
        else:
            self.__salary = None
            
    def get_employee_id(self):
        return self.__employee_id
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def display(self):
        print(f"Employee ID: {self.get_employee_id()} | Name: {self.get_name()} | Salary: {self.get_salary()}")
    
    
em1 = Employee(1,"Arman", 500000)
em1.display()