from math import sqrt
from typing import Iterable


class Vector:
    """
    Represents a vector in a multidimensional space.
    """

    def __init__(self, coordinates: Iterable[float]) -> None:
        """
        Creates a vector from a sequence of numeric coordinates.
        """
        self.coordinates = tuple(coordinates)
        self.dimension = len(self.coordinates)

    def __add__(self, other: "Vector") -> "Vector":
        """
        Returns the sum of two vectors.
        """
        return Vector(a + b for a, b in zip(self.coordinates, other.coordinates))

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Returns the difference of two vectors.
        """
        return Vector(a - b for a, b in zip(self.coordinates, other.coordinates))

    def __mul__(self, other: "Vector") -> float:
        """
        Computes the scalar (dot) product of two vectors.
        """
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def __rmul__(self, scalar: float) -> "Vector":
        """
        Returns the result of multiplying the vector by a scalar.
        """
        return Vector(a * scalar for a in self.coordinates)

    def get_length(self) -> float:
        """
        Returns the magnitude of the vector.
        """
        return sqrt(sum(a ** 2 for a in self.coordinates))

    def __eq__(self, other: object) -> bool:
        """
        Compares two vectors by their lengths.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.get_length() == other.get_length()

    def __lt__(self, other: "Vector") -> bool:
        """
        Checks if this vector is shorter than another vector.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.get_length() < other.get_length()

    def __repr__(self) -> str:
        """
        Returns a string representation of the vector.
        """
        return f"Vector({self.coordinates})"


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(2 * v1)
print(v1 < v2)
