def reverse_string(my_string):
    i = len(my_string) - 1
    while i >= 0:
        yield my_string[i]
        i -= 1


for c in reverse_string("Elzero"):
    print(c)


#######OR########
def reverse_string(my_string):
    for char in reversed(my_string):
        yield char


# Reverse The String
for c in reverse_string("Elzero"):
    print(c)

############################# 2 ###########################
def my_decorator(func):
    def wrapper():
        print("Sugar Added From Decorators")

        func()

        print(15 * "#")

    return wrapper


@my_decorator
def make_tea():
    print("Tea Created")


@my_decorator
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()

# Needed Output

# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"
