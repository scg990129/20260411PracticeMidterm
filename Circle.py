# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260411


import math
from Point2D import Point

class Circle:
    def __init__(self, edgePointFromCenter: "Point"):
        # Using only instances of the  point class as your fields/properties, write a class representing a circle object.
        self._EdgePointFromCenter = edgePointFromCenter
        self._Radius = self._EdgePointFromCenter.getDistance(Point(0, 0))
        # Let the fields be capitalized since they should be constant and hide them with underscores.

    # Provide an area and a perimeter method (function member).
    def area(self)-> float:
        return math.pi * self._Radius ** 2

# Provide an area and a perimeter method (function member).
    def perimeter(self)-> float:
        return 2 * math.pi * self._Radius


def test_circle():
    # 1. Setup: Create an edge point.
    # A point at (3, 4) should result in a radius of 5.0 from the origin (0,0).
    edge = Point(3, 4)
    my_circle = Circle(edge)

    # 2. Expected Values
    expected_radius = 5.0
    expected_area = math.pi * (expected_radius ** 2)  # approx 78.54
    expected_perimeter = 2 * math.pi * expected_radius  # approx 31.42

    # 3. Execution & Verification
    print("--- Circle Test Case ---")
    print(f"Edge Point: ({edge.getX()}, {edge.getY()})")

    # Check Area
    print(f"Calculated Area: {my_circle.area():.2f}")
    assert math.isclose(my_circle.area(), expected_area), "Area calculation failed!"

    # Check Perimeter
    print(f"Calculated Perimeter: {my_circle.perimeter():.2f}")
    assert math.isclose(my_circle.perimeter(), expected_perimeter), "Perimeter calculation failed!"

    print("\nResult: All tests passed successfully!")


if __name__ == "__main__":
    test_circle()