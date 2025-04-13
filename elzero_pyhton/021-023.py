friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]


print(friends[0])
print(friends[-5])

print(friends[-1])
print(friends[4])


# assign 2

print("*" * 50)

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]


print(friends[0], friends[2], friends[4])
print(friends[1], friends[3])


print("*" * 50)

# assign 3

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]


print(friends[1:4])
print(friends[-2:])


# assign 4
print(f"*" * 20 + "assignment4" + 20 * "*")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]


friends[3:] = "Elzero", "Elzero"

print(friends)

# assign 5
print(f"*" * 20 + "assignment5" + 20 * "*")


friends = ["Osama", "Ahmed", "Sayed"]


print(friends)
friends.append("Salem")
friends.insert(0, "Nasser")
print(friends)

# assign 6
print(f"*" * 20 + "assignment6" + 20 * "*")
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]


friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)


# assign 7
print(f"*" * 20 + "assignment7" + 20 * "*")

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]


friends.extend(employees)
friends.extend(school)
print(friends)


# assign 8
print(f"*" * 20 + "assignment8" + 20 * "*")


friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# assign 9
print(f"*" * 20 + "assignment 9" + 20 * "*")


friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]


print(len(friends))


#assign 10 

print(f"*" * 20 + "assignment 10" + 20 * "*")


technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]


print(technologies[4][0])
print(technologies[4][2])