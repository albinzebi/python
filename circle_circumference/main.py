import math

def print_circum(radius):
    circumference = 2 * math.pi * radius
    print(f"For a circle with a radius of {radius}, the circumference is {circumference:.5f}.")

print_circum(1)
print_circum(2)
print_circum(10)