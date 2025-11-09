def calculate(x, y, op=""):
    op = op.lower()

    if (
        op == "+" or op == "add" or op == "a"
    ):  # or you can use in if op in ["+", "add", "a"]:
        return f"{x + y}"
    elif op == "-" or op == "subtract" or op == "s":
        return f"{x - y}"
    elif op == "*" or op == "multiply" or op == "m":
        return f"{x * y}"
    elif op == "":
        return f"{x + y}"
    else:
        return "invalid operator"


# Tests
# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "AdD")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30

# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10

# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200

# ==============#=====================#===============#


def addition(*numbers):
    v = 0

    for i in numbers:
        if i != 10:
            if i != 5:
                v += i
            else:
                v -= 5
    return v


#
# print(addition(10, 20, 30, 10, 15))  #  65
# print(addition(10, 20, 30, 10, 15, 5, 100))  #  160

# ==============#=====================#===============#


def show_skills(name, *skills):
    result = f"Hello {name}, "
    if not skills:
        return result + "You don't have any skills"

    result += "Your Skills Are:\n"
    for skill in skills:
        result += f"- {skill}\n"
    return result


# print(show_skills("Gehad", "Python", "SQL"))
# print(show_skills("ge"))


# ==============#=====================#===============#
def say_hello(name="Unkown", age="Unknow", country="Unknown"):
    return f"Hello {name} Your age Is {age} And You Live In {country}"


print(say_hello("Gehad", 24, "Egypt"))
print(say_hello())
