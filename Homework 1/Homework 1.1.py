import math


def calculate_circle_area(radius: int|float)-> float:
    """
    Calculate the area of a circle given its radius.
    Returns:
        float: The area of the circle """
    return math.pi * radius**2


radius = float(input("Input radius: "))
area = calculate_circle_area(radius)
print(f"The area of a circle {area:.2f}")

