import random

print(f'"Random Number Between 10 And 50 => {random.randint(10,50)}')

# sol 1
even_num = random.choice(range(2, 11, 2))  # 2 --> the last 2 for step
print(f'"Random Even Number Between 2 And 10 => {even_num}')

# anothe_sol 2
random.choice([2, 4, 6, 8, 10])

odd_number = random.choice([n for n in range(1, 10) if n % 2 != 0])
print(f"Random Odd Number Between 1 And 9 => {odd_number}")

# =================

# the 2,3 and 4 assignments in Python folder

# ===================
