class Employee:

    company_name = "TechCorp"  # class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

    def __str__(self):
        return f"{self.name} - {self.company_name} - {self.salary}"
    



emp1 = Employee("Ahmed", 5000)
print(emp1)

Employee.change_company("MegaTech")
print(emp1.company_name)

print(Employee.is_valid_salary(3000))  # True
print(Employee.is_valid_salary(-10))   # False