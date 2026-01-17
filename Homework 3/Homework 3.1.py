class Fraction:
    """
    A class for representing and working with fractions.
    Operations for adding, opening, multiplying, and dividing fractions.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initialize the Fraction instance with numerator and denominator.
        """
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions and return the result.
        """
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Subtract another fraction from this one and return the result.
        """
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Multiplication of fractions
        """
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Division of fractions

        """
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __repr__(self) -> str:
        """Return representation of the fraction"""
        return f"{self.numerator}/{self.denominator} "


fr1 = Fraction(2, 3)
fr2 = Fraction(3, 2)

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
