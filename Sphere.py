# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260411
from Point2D import Point

import math

from Circle import Circle

class Sphere:
    def __init__(self, refCircle : "Circle"):
        self._refCircle = refCircle

    def volume(self)-> float:
        radius = self._refCircle.perimeter() / (2 * math.pi)
        circle_area = self._refCircle.area()
        return (4 / 3) * radius * circle_area

    def surfaceArea(self)->float:
        return 4 * self._refCircle.area()

def test_sphere():
    # 1. Setup: Circle with radius 5 (using Point 3,4)
    edge = Point(3, 4)
    base_circle = Circle(edge)
    my_sphere = Sphere(base_circle)

    # 2. Expected Values (Radius = 5.0)
    # Surface Area = 4 * pi * 5^2 = 100 * pi (approx 314.16)
    expected_sa = 4 * math.pi * (5.0 ** 2)
    # Volume = (4/3) * pi * 5^3 = (500/3) * pi (approx 523.60)
    expected_vol = (4 / 3) * math.pi * (5.0 ** 3)

    # 3. Execution
    print(f"--- Sphere Test Case (Radius: 5.0) ---")

    calc_sa = my_sphere.surfaceArea()
    calc_vol = my_sphere.volume()

    print(f"Surface Area: {calc_sa:.4f} (Expected: {expected_sa:.4f})")
    print(f"Volume:       {calc_vol:.4f} (Expected: {expected_vol:.4f})")

    # 4. Verification
    assert math.isclose(calc_sa, expected_sa), "Surface Area test failed!"
    assert math.isclose(calc_vol, expected_vol), "Volume test failed!"

    print("\nResult: Sphere logic is mathematically sound!")


if __name__ == "__main__":
    test_sphere()