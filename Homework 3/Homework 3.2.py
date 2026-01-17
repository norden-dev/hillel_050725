import math
from typing import Union


class Vector:
    """
    A class for representing a vector in space with the ability to perform
    basic operations such as addition, subtraction, multiplication by a scalar
    and comparison of vectors by length.
    """

    def __init__(self, *args: Union[int, float]) -> None:
        """Initialize the Vector """
        self.args = args

    def __add__(self, other: "Vector") -> "Vector":
        """Add two vectors"""
        result = [a + b for a, b in zip(self.args, other.args)]
        return Vector(*result)

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtract two vectors"""
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must be of the same dimension.")
        result = [a - b for a, b in zip(self.args, other.args)]
        return Vector(*result)

    def __mul__(self, scalar: int) -> "Vector":
        """Multiplies a vector by a scalar."""
        result = [a * scalar for a in self.args]
        return Vector(*result)

    def length(self) -> float:
        """Calculates the length of a vector."""
        return math.sqrt(sum(a ** 2 for a in self.args))

    def __eq__(self, other) -> bool:
        """Compare vectors by their length"""
        return self.length() == other.length()

    def __lt__(self, other) -> bool:
        """ Compares vectors by their length."""
        return self.length() < other.length()

    def __repr__(self) -> str:
        """Return representation of the vector."""
        return f"{self.args}"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1.length())
print(v1 == v2)
print(v1 < v2)
