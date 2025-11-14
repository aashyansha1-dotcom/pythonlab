from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.threeDgraphics.cuboid import surface_area as cuboid_area, volume as cuboid_vol
from graphics.threeDgraphics.sphere import surface_area as sphere_area, volume as sphere_vol

print("Rectangle area:", rect_area(8, 6))
print("Rectangle perimeter:", rect_perimeter(8, 6))

print("Circle area:", circle_area(4))
print("Circle perimeter:", circle_perimeter(4))

print("Cuboid surface area:", cuboid_area(2, 3, 4))
print("Cuboid volume:", cuboid_vol(2, 3, 4))

print("Sphere surface area:", sphere_area(3))
print("Sphere volume:", sphere_vol(3))
