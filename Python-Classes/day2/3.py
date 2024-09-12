# Create a class Student with private attributes name, roll_number, and grades. Implement methods to add grades, calculate the average grade, and display the student’s information. Ensure that the grades are between 0 and 100.
class Student:
    def __init__(self, name: str, roll_number: int) -> None:
        self.set_name(name)
        self.set_roll_number(roll_number)
        self.__grades = [] 


    def set_name(self, name: str) -> None:
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            self.__name = None


    def set_roll_number(self, roll_number: int) -> None:
        if isinstance(roll_number, int) and roll_number > 0:
            self.__roll_number = roll_number
        else:
            self.__roll_number = None


    def add_grade(self, grade: float) -> None:
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Invalid grade. Grades must be between 0 and 100.")

 
    def calculate_average(self) -> float:
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0  

  
    def get_name(self) -> str:
        return self.__name

 
    def get_roll_number(self) -> int:
        return self.__roll_number


    def display(self) -> None:
        average_grade = self.calculate_average()
        print(f"Student Name: {self.get_name()} | Roll Number: {self.get_roll_number()} | Average Grade: {average_grade:.2f}")
        print(f"Grades: {self.__grades}")


student1 = Student("John Doe", 101)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
student1.display()

student1.add_grade(105) 
student1.display()
