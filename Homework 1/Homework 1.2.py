class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize rectangle with width and height

        :param width: Rectangle width
        :param height: Rectangle height
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculates the area of a rectangle."""
        return self.width * self.height

    def perimetr(self) -> float:
        """Calculates perimetr of a rectangle"""
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """Checking for square or not"""
        return  self.width == self.height

    def resize(self, new_width: float, new_height: float) -> None:
        """Resize width and height"""
        self.width = new_width
        self.height = new_height


rect = Rectangle(2, 4)

print(rect.area())
print(rect.perimetr())
print(rect.is_square())
print(rect.resize(5, 3))
print(rect.width, rect.height)
