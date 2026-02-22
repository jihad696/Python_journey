class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")


class Employee(Person):

    def __init__(self,name,age,company,salary):
        super().__init__(name,age)
        self.company = company
        self.salary = salary



class Manager(Employee):

    def __init__(self,name,age,company,salary,department):
        super().__init__(name,age,company,salary)
        self.department = department


    def manage(self):
        print("manage")


class Developer(Employee):
    def __init__(self,name,age,company,salary,language):
        super().__init__(name,age,company,salary)
        self.language = language
    def code(self):
        print("code()")


class Investor:
    def __init__(self,portfolio):
        self.portfolio = portfolio

    def invest(self):
        print("Hey from self ")

class FounderCEO(Manager,Investor):
    def __init__(self, name, age, company, salary, department, portfolio):
        Manager.__init__(self, name, age, company, salary, department)
        Investor.__init__(self, portfolio)
    

ahmed = FounderCEO('ahmed',20,'koko',523,'it','jjk')
 
ahmed.introduce()


