class BankAccount:
    def __init__(self) -> None:
        self.__balance: float = 0.0

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self) -> float:
        return self.__balance
    



acc = BankAccount()

# acc.deposit(-100) 

acc.deposit(500)
acc.withdraw(200)  
acc.withdraw(200)

print(acc.get_balance())