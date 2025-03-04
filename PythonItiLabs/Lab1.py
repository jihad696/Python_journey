# Q1
bill = 47.28
tip = bill * 0.15
total = bill + tip
each_person_pays = total / 2
print(f"Each person needs to pay: {each_person_pays} dollars")

# Q2
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if num1.isdecimal() and num2.isdecimal():
    num1 = float(num1)
    num2 = float(num2)

    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid input. Please enter numbers only.")


# Q3
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = " {}"
word6 = "so"
word7 = "far?"
sentence = (
    word1
    + " "
    + word2
    + "  "
    + word3
    + ""
    + word4
    + ""
    + word5
    + ""
    + word6
    + ""
    + word7
)
print(sentence)

# Q4
sentence_js = 'console.log("{} {} {} {}{} {} {}!");'.format(
    word1, word2, word3, word4, word5, word6, word7[:-1]
)

print(sentence_js)


# Q
statement = input("Enter a statement: ")
print(f"Length of the statement: {len(statement)}")

# Q6
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(f"Result: {(num1 + num2)}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation.")
