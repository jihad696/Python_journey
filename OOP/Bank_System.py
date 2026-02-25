from abc import ABC,abstractmethod
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def introduce(self):
        return f"I'm {self.name} my age is {self.age}"


person1 = Person("Hala",23)
print(person1.introduce())

class Account(ABC):

    def __init__(self,balance):
        self._balance = None #private
        self.balance = balance

    @abstractmethod
    def deposite(self,dep):
        if dep >= 0:
            self.total += dep 
        return f"Your deposite is {dep} and yur total now is {self.total}"
    

    # @abstractmethod
    # def withdraw(self,withdraw):
    #     return 

    # @abstractmethod
    # def get_balance(self):
    #     pass

class testacc(Account):


# class SavingsAccount(Account,Person):

#     def interest_rate():
#         pass

#     def apply_interest():
#         pass

# class CurrentAccount(Account, Person):
#     def overdraft_limit():
#         pass




