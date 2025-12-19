# values = (0, 1, 2)

# if any(values):  # true cuz at least one var is true

#     my_var = 0

# my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]  # the condition is true so my_var = 0


# if (
#     all(my_list[:4]) or all(my_list[:6]) or all(my_list[:])
# ):  # True or True or True all are true

#     print("Good")

# else:

#     print("Bad")

# # ==============================================
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820
# # ==============================================
# n = 21

# l = list(range(n))  # [1,2,3,..,20]

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):  # sum(1..20)/21

#     print("Good")

# =============================


def my_all(*args):
    if not args:
        return False

    iterable = args[0] if len(args) == 1 else args

    try:
        for item in iterable:
            if isinstance(item, (list, tuple, set)):
                for sub in item:
                    if not sub:
                        return False
            else:
                if not item:
                    return False
    except TypeError:
        if not iterable:
            return False

    return True


# my_all
print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False


# قم بعمل Function تقوم بنفس آلية عمل ال all وقم بتسميتها my_all
# قم بعمل Function تقوم بنفس آلية عمل ال any وقم بتسميتها my_any
# قم بعمل Function تقوم بنفس آلية عمل ال min وقم بتسميتها my_min
# قم بعمل Function تقوم بنفس آلية عمل ال max وقم بتسميتها my_max
# تأكد ان my_min + my_max تقبل List أو Tuple


# # my_any
# print(my_any([0, 1, [], False]))  # True
# print(my_any([(), 0, False]))  # False

# # my_min
# print(my_min([10, 100, -20, -100, 50]))  # -100
# print(my_min((10, 100, -20, -100, 50)))  # -100

# # my_max
# print(my_max([10, 100, -20, -100, 50, 700]))  # 700
# print(my_max((10, 100, -20, -100, 50, 700)))  # 700
