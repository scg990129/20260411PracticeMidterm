# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260411

import math

# Write a class representing a 2D point.
class Point:
    def __init__(self, x: int, y: int):
        self._X = x
        self._Y = y
        # Have the class consist of two fields representing it's coordinate, ideally x and y.

    def getX(self):
        return self._X

    def getY(self):
        return self._Y

# Write a method (function members)  that finds the distance from one point to the other.
    def getDistance(self, other: 'Point')-> float:
        return math.sqrt((self._X - other._X)**2 + (self._Y - other._Y)**2)

# Write a method that finds the slope given another point.
    def slope(self, other: 'Point')-> float:
        return math.inf if (other._X == self._X) else (other._Y - self._Y) / (other._X - self._X)

# Phase 1
import math
class Point2D:
    # Let the fields (data members) be public, but make sure that they don't fall victims to immutability so set the fields to be constant.
    # Have the class consist of two fields representing it's coordinate, ideally x and y.
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    # Write a method (function members)  that finds the distance from one point to the other.
    def getDistance(self, other: 'Point2D')-> float | int:
        temp = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return int(temp) if math.isclose(int(temp), temp) else temp

    # Write a method that finds the slope given another point.
    def slope(self, other: 'Point2D')-> float | int:
        return math.inf if (other.x == self.x) else i if math.isclose(temp := (other.y - self.y) / (other.x - self.x), i:=int(temp)) else temp

    def __str__(self):
        return f"({self.x}, {self.y})"

# Phase 2
import math
# Using only instances of the  point class, write a class representing a Geometric Sector object.
class GeometricSector:
    def __init__(self, point1: Point2D, point2: Point2D, center: Point2D = Point2D(0, 0)):
        self._point1 = point1
        self._point2 = point2
        self._center = center
        if not math.isclose(d1:=point1.getDistance(center), d2:=point2.getDistance(center)):
            raise ValueError(f"Points must have same radius: ({d1} ≠ {d2})")
        # You can let the fields be public, but make sure that they don't fall victims to immutability so set the fields to be constant.

    @property
    def point1(self) -> Point2D:
        return self._point1

    @property
    def point2(self) -> Point2D:
        return self._point2

    @property
    def center(self) -> Point2D:
        return self._center

# Provide an area and a perimeter method (function member).
    def getArea(self) -> int | float:
        if (radius := self.point1.getDistance(self.center)) == 0:
            return 0
        chordLength = self.point1.getDistance(self.point2)
        cosAngle = (2 * (radius ** 2) - (chordLength ** 2)) / (2 * (radius ** 2))
        angle = math.acos(1 if cosAngle >= 1 else -1 if cosAngle <= -1 else cosAngle)
        area = 0.5 * (radius**2) * angle
        return i if math.isclose(area, i:=int(area)) else area

    def getPerimeter(self) -> int | float:
        if (radius := self.point1.getDistance(self.center)) == 0 or (self.point1.y == self.point2.y and self.point1.x == self.point2.x):
            return 0
        chordLength = self.point1.getDistance(self.point2)
        cosAngle = (2*(radius**2) - (chordLength**2)) / (2 * (radius**2))
        angle = math.acos(1 if cosAngle >= 1 else -1 if cosAngle <= -1 else cosAngle)
        perimeter = radius * angle + (2 * radius)
        return i if math.isclose(perimeter, i:= int(perimeter)) else perimeter

    def __str__(self):
        return f"center({self.center}), point1({self.point1}), point2({self.point2})"

if __name__ == "__main__":
    # p1 = Point2D(1,2)
    # print(p1)
    # print(p1:= Point2D(3,4))
    # print(p1.getDistance(Point2D(0,0)))
    # p1 = Point2D(1,1)
    # print(p1.slope(Point2D(0,0)))
    # p1 = Point2D(1,0)
    # print(p1.slope(Point2D(0,0)))
    # p1 = Point2D(0,1)
    # print(p1.slope(Point2D(0, 0)))
    # p1 = Point2D(1,2)
    # print(p1.slope(Point2D(0, 0)))

    try:
        # 1. Initialize Points
        center = Point2D(0, 0)
        p1 = Point2D(4, 0)
        p2 = Point2D(0, 4)

        # 2. Create Sector
        sector = GeometricSector(p1, p2, center)
        print(f"Testing Sector: {sector}")

        # 4. Test Area
        area = sector.getArea()
        expected_area = 4 * math.pi
        print(f"Area: {area:.4f} (Expected: ~{expected_area:.4f})")

        # 5. Test Perimeter
        perimeter = sector.getPerimeter()
        expected_perimeter = (2 * math.pi) + 8
        print(f"Perimeter: {perimeter:.4f} (Expected: ~{expected_perimeter:.4f})")

        # 6. Test Immutability (Requirement Check)
        print("\nChecking Immutability...")
        try:
            sector.center = Point2D(1, 1)
        except AttributeError:
            print("Success: Cannot modify sector center.")

    except ValueError as e:
        print(f"Validation Error: {e}")

