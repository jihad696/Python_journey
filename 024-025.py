# assign 1
tuple3 = ("Gehad",)
print(tuple3[0])
print(type(tuple3))
print("*" * 20)

# assign 2
friends = ("Osama", "Ahmed", "Sayed")
# convert tuple to list to update
friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)
print(friends)
print(type(friends))

print(f"{len(friends)} Elements")


# assign 3
print("*" * 20)

nums = (1, 2, 3)
letters = ("A", "B", "C")

a = nums + letters
print(f"nums_and_letters_one = {a}")

print(f"{len(a)} Elements ")


# assign 4
print("*" * 20)

my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple

print(a)
print(b)
print(c)
