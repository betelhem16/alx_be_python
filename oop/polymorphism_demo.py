"""
Demonstrates polymorphism and method overriding in Python.
"""

import math


class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)
