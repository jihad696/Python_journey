def calcarea(shape, dim1, dim2=None):
    import math

    if shape == "t":
        if dim2 is None:
            return "Error: Triangle requires both base and height"
        return 0.5 * dim1 * dim2

    elif shape == "r":
        if dim2 is None:
            return "Error: Rectangle requires both length and width"
        return dim1 * dim2

    elif shape == "s":
        return dim1 * dim1

    elif shape == "c":
        return math.pi * dim1 * dim1

    else:
        return "Error: Invalid shape. Use 't' for triangle, 'r' for rectangle, 's' for square, or 'c' for circle"


print(calcarea("r", 0.2))
