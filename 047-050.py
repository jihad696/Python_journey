#1

num = int(input("Enter a number: "))  # Input from user
i = num - 1
count = 0

if num > 0:
    while i > 0:
        if i == 6:
            i -= 1
            continue
        print(i)
        count += 1
        i -= 1
    print(f'"{count} Numbers Printed Successfully."')
else:
    print("please enter num greater than 0")


#2
print("=" * 20)

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i = 0
ignored = 0  

while i < len(friends):
    if friends[i][0].islower():
        ignored += 1
    else:
        print(friends[i])
    i += 1

print(f"{ignored} name(s) ignored.")


print("=" * 20)
#3

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop())


# 4
print("=" * 20)


my_friends = []
count = 4
while len(my_friends) != 4:
    name = input().strip()
    if name.isupper():
        print("Invalid Name")

    elif name.islower():
        my_friends.append(name.capitalize())
        count -=1
        print(f"Friend {name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {count}")

    elif name[0].isupper():
        my_friends.append(name)
        count -=1
        print("Friend {} is added".format(name))
        print(f"Names Left in List Is {count}")

    else:
        print("try again! no data added")
print(my_friends)
