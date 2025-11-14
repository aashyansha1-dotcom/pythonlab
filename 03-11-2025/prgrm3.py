from graphics.rectangle import *
from graphics.circle import *
from graphics.threeDgraphics.cuboid import *
from graphics.threeDgraphics.sphere import *

print("Rectangle area:", area(5, 10))
print("Rectangle perimeter:", perimeter(5, 10))

print("Circle area:", area(6))
print("Circle perimeter:", perimeter(6))

print("Cuboid surface area:", surface_area(2, 3, 4))
print("Cuboid volume:", volume(2, 3, 4))

print("Sphere surface area:", surface_area(4))
print("Sphere volume:", volume(4))
