import math

π = math.pi

def circle_area(radius):
    return π * radius**2

def circle_circumference(radius):
    return 2 * π * radius

radius = 5
area = circle_area(radius)
circumference = circle_circumference(radius)

print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")