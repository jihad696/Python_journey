friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]


# def remove_chars(msg):
#     return msg[1:-1]

# cleaned_list = list(map(remove_chars,friends_map))

cleaned_list = list(map(lambda msg: msg[1:-1], friends_map))

print(cleaned_list)

for friend in cleaned_list:
    print(friend)

###########################################

print("#" * 18)
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


# def get_names(name):
#     return name.endswith("m")


# names = list(filter(get_names, friends_filter))
names = list(filter(lambda name: name.endswith("m"), friends_filter))

for i in names:
    print(i)


################

print("#" * 15)

nums = [2, 4, 6, 2]

from functools import reduce


def multply(x, y):
    return x * y


# res = reduce(multply, nums)
res = reduce(lambda x, y: x * y, nums)

print(res)


# Output
96

################

print("#" * 15)
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for i, v in enumerate(skills, start=50):
    print(i, v)
