class Student:
    def __init__(self, name, age, *grades):
        self.name = name
        self.age = age
        self.grades = list(grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def status(self):
        if self.average() >= 60:
            return "Pass"
        else:
            return "Fail"
    
    def info(self):
        return f"{self.name}, Age: {self.age}, Grades: {self.grades}, Average: {self.average()}, Status: {self.status()}"
    




s1 = Student("Alice", 20, 70, 80, 90)
s1.add_grade(50)
print(s1.info())