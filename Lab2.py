# Q1

user_input = input("Enter a word: ")
char = input("Enter a letter: ")

indices = []
for index, letter in enumerate(user_input):
    if letter == char:
        indices.append(index)

print(indices)


# Q2
n = int(input("Enter a number: "))

result = []
for i in range(1, n + 1):
    row = []
    for j in range(1, i + 1):
        row.append(i * j)
    result.append(row)

print(result)


# Q3

names = eval(input("Enter list of names: "))
result = {}

for name in names:
    alpha = name[0].lower()

    result.setdefault(alpha, []).append(name)

result = dict(sorted(result.items()))
print(result)
