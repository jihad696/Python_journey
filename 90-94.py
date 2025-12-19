# NUM = input("Add Your Number: ")
#
# try:
#     NUM_INT = int(NUM)
# except ValueError:
#     raise ValueError("it isn't a number!") from None
#
# if NUM_INT == 0:
#     raise ValueError("Number Must Be Larger Than 0")
#
# if NUM_INT < -9 or NUM_INT > 9:
#     raise IndexError("Only One Character Allowed")
#
# if NUM_INT < 0:
#     raise Exception("cannot be less than zero")
#
# print("#" * 8)
# print(NUM_INT)
# print("#" * 8)
#==================================================
LETTER = input("Add Letter From A to Z").strip()

# Your Code Here

try:
    if len(LETTER) != 1:
        raise IndexError

    if LETTER.islower():
        raise ValueError

except IndexError:
    raise IndexError ("You Must Write One Character Only") from None
except ValueError:
    raise ValueError ("The Letter Not In A - Z") from None

else:
    print(f"You Typed {LETTER}")

#==================================================
def calculate(num1: float, num2: float) -> float:
    return num1 + num2

print(calculate(20, 30))
















