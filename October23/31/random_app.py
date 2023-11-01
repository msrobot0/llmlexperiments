import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def main():
    print("Circle Area Calculator")
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}")

if __name__ == "__main__":
    main()

