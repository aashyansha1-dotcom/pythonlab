from area_import import area_of_rectangle, area_of_circle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))

rect_area = area_of_rectangle(length, breadth)
circle_area = area_of_circle(radius)

print(f"\nArea of Rectangle = {rect_area}")
print(f"Area of Circle = {circle_area}")
