import math

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(width, height):
    return width * height

def square_area(side):
    return side ** 2

def circle_area(radius):
    return math.pi * radius ** 2

def calculate_area():
    print("Choose a shape:")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Circle")
    
    option = input("Enter the option number (1-4): ").strip()

    if option == "1":
        base = eval(input("Enter the base: "))
        height = eval(input("Enter the height: "))
        print(f"Area of Triangle = {triangle_area(base, height)}")

    elif option == "2":
        width = eval(input("Enter the width: "))
        height = eval(input("Enter the height: "))
        print(f"Area of Rectangle = {rectangle_area(width, height)}")

    elif option == "3":
        side = eval(input("Enter the side length: "))
        print(f"Area of Square = {square_area(side)}")

    elif option == "4":
        radius = eval(input("Enter the radius: "))
        print(f"Area of Circle = {circle_area(radius)}")

    else:
        print("Invalid option! Please enter a number between 1 and 4.")

calculate_area()
