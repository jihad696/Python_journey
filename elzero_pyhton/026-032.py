# assign 1

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.remove(5)
print(unique_list)

# assign 2
print("=" * 12)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

nums.update(letters)
print(nums)
print(nums.union(letters))
print(nums | letters)

# assign 3
print("=" * 25)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)

my_set.clear()
print(my_set)
my_set.update(letters)
print(my_set)
my_set.discard("C")
print(my_set)


# assign 4
print("=" * 25)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_two.issuperset(set_one))

# assign 5
print("=" * 25)

Dict = {
    "one": {"name": "HTML", "progress": "Progress is 90%"},
    "two": {"name": "Css", "progress": "Progress is 80%"},
    "three": {"name": "Python", "progress": "Progress is 30%"},
    "four": {"name": "AI", "progress": "Progress is 30%"},
}

print(Dict["one"]["name"], Dict["one"]["progress"])
print(Dict["two"]["name"], Dict["two"]["progress"])
print(Dict["three"]["name"], Dict["three"]["progress"])
print(Dict["four"]["name"], Dict["four"]["progress"])




