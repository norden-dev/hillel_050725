class Rectangle:
    """A class representing a rectangle."""


    def __init__( self, width: float, height: float) -> None:
        """
        :param width: Rectangle width (positive number)
        :param height: Rectangle height (positive number)"""
        self.width = width
        self.height = height

    def area(self)-> float:
        """Calculates the area of a rectangle."""
        return self.width * self.height

    def perimetr(self)-> float:
        """Calculates perimetr of a rectangle"""
        return 2* (self.width + self.height)

    def is_square(self)->bool:
        """Checking for square or not"""
        return True if self.width == self.height else False

    def resize(self, new_width, new_height) -> None:
        """Resize width and height"""
        self.width = new_width
        self.height = new_height


react = Rectangle(2, 4 )
print(react.area())
print(react.perimetr())
print(react.is_square())
print(react.resize(5,3))
print(react.width, react.height)