
#control flow


num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())

operation = input("Enter the operation (+, -, *, /, %): ").strip()

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
elif operation == "%":
    if num2 != 0:
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Error: Cannot use modulus with zero.")
else:
    print("Invalid operation. Please use one of +, -, *, /, %")



print("="*20)

age = 17

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

print("="*20)


age = int(input())

months = age * 12
weeks = age * 48
days = age * 365
hours = days * 24
mins = hours * 60
secs = mins * 60

print(f"Your Age In Months Is {months} Months")
print(f"Your Age In weeks Is {weeks} weeks")
print(f"Your Age In days Is {days} days")
print(f"Your Age In hours Is {hours} hours")
print(f"Your Age In minuts Is {mins} minuts")
print(f"Your Age In seconds Is {secs} seconds")


print("="*20)


country = input("Input Your Country").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
   
    print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}$")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")





