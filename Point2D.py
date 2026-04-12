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
