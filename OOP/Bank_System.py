from abc import ABC, abstractmethod
import math

# ─────────────────────────────────────────
# Base Class
# ─────────────────────────────────────────

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"


# ─────────────────────────────────────────
# Abstract Class
# ─────────────────────────────────────────

class Account(ABC):

    _total_accounts = 0  # class variable

    def __init__(self):
        Account._total_accounts += 1

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be greater than 0")

    @classmethod
    def get_total_accounts(cls):
        return cls._total_accounts


# ─────────────────────────────────────────
# SavingsAccount
# ─────────────────────────────────────────

class SavingsAccount(Account, Person):

    def __init__(self, name, age, balance, interest_rate):
        Person.__init__(self, name, age)
        Account.__init__(self)
        self._balance = balance
        self._interest_rate = None
        self.interest_rate = interest_rate  # triggers setter

    # ── deposit ──
    def deposit(self, amount):
        Account.validate_amount(amount)
        self._balance += amount

    # ── withdraw ──
    def withdraw(self, amount):
        Account.validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    # ── get_balance ──
    def get_balance(self):
        return self._balance

    # ── interest_rate property ──
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if value < 0 or value > 100:
            raise ValueError("Interest rate must be between 0 and 100")
        self._interest_rate = value

    # ── apply_interest ──
    def apply_interest(self):
        self._balance *= (1 + self._interest_rate / 100)

    # ── dunder methods ──
    def __str__(self):
        return f"{self.name}'s Savings Account | Balance: ${self._balance:.2f}"

    def __repr__(self):
        return f"SavingsAccount('{self.name}', {self.age}, {self._balance}, {self._interest_rate})"

    def __gt__(self, other):
        return self._balance > other.get_balance()

    def __add__(self, other):
        merged = SavingsAccount(
            f"{self.name} & {other.name}",
            0,
            self._balance + other.get_balance(),
            self._interest_rate
        )
        return merged


# ─────────────────────────────────────────
# CurrentAccount
# ─────────────────────────────────────────

class CurrentAccount(Account, Person):

    def __init__(self, name, age, balance, overdraft_limit):
        Person.__init__(self, name, age)
        Account.__init__(self)
        self._balance = balance
        self._overdraft_limit = None
        self.overdraft_limit = overdraft_limit  # triggers setter

    # ── deposit ──
    def deposit(self, amount):
        Account.validate_amount(amount)
        self._balance += amount

    # ── withdraw ──
    def withdraw(self, amount):
        Account.validate_amount(amount)
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self._balance -= amount

    # ── get_balance ──
    def get_balance(self):
        return self._balance

    # ── overdraft_limit property ──
    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value):
        if value < 0:
            raise ValueError("Overdraft limit can't be negative")
        self._overdraft_limit = value

    # ── dunder methods ──
    def __str__(self):
        return f"{self.name}'s Current Account | Balance: ${self._balance:.2f} | Overdraft: ${self._overdraft_limit}"

    def __gt__(self, other):
        return self._balance > other.get_balance()


# ─────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────

print("=" * 50)
print("Creating Accounts")
print("=" * 50)

s1 = SavingsAccount("Ahmed", 25, 1000, 5)
s2 = SavingsAccount("Sara", 30, 500, 3)
c1 = CurrentAccount("Ali", 28, 2000, 500)

print(s1.introduce())
print(s2.introduce())
print(c1.introduce())

print("\n" + "=" * 50)
print("Deposit & Withdraw")
print("=" * 50)

s1.deposit(500)
print(f"After deposit: {s1.get_balance()}")

s1.withdraw(200)
print(f"After withdraw: {s1.get_balance()}")

print("\n" + "=" * 50)
print("Apply Interest")
print("=" * 50)

s1.apply_interest()
print(f"After 5% interest: {s1.get_balance():.2f}")

print("\n" + "=" * 50)
print("Overdraft Test")
print("=" * 50)

c1.withdraw(2400)  # allowed (within 500 overdraft)
print(f"After overdraft withdraw: {c1.get_balance()}")

try:
    c1.withdraw(200)  # should fail
except ValueError as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("Dunder Methods")
print("=" * 50)

print(s1)
print(s2)
print(f"s1 > s2: {s1 > s2}")

merged = s1 + s2
print(f"Merged account balance: ${merged.get_balance():.2f}")

print("\n" + "=" * 50)
print("Class & Static Methods")
print("=" * 50)

print(f"Total accounts created: {Account.get_total_accounts()}")

try:
    Account.validate_amount(-50)
except ValueError as e:
    print(f"Validation error: {e}")