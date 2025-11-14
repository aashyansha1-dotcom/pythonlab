import graphics.rectangle
import graphics.circle
import graphics.threeDgraphics.cuboid
import graphics.threeDgraphics.sphere

print("Rectangle area:", graphics.rectangle.area(10, 5))
print("Rectangle perimeter:", graphics.rectangle.perimeter(10, 5))

print("Circle area:", graphics.circle.area(7))
print("Circle perimeter:", graphics.circle.perimeter(7))

print("Cuboid surface area:", graphics.threeDgraphics.cuboid.surface_area(2, 3, 4))
print("Cuboid volume:", graphics.threeDgraphics.cuboid.volume(2, 3, 4))

print("Sphere surface area:", graphics.threeDgraphics.sphere.surface_area(5))
print("Sphere volume:", graphics.threeDgraphics.sphere.volume(5))
