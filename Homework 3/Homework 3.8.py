from decimal import Decimal, ROUND_HALF_UP


class Price:
    """Represents a monetary value with fixed two‑decimal precision."""

    def __init__(self, amount: float | str | Decimal) -> None:
        """Creates a new Price instance with rounding to two decimal places."""
        self.amount = Decimal(str(amount)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    def add(self, other: "Price") -> "Price":
        """Returns a new Price representing the sum of two Price values."""
        return Price(self.amount + other.amount)

    def subtract(self, other: "Price") -> "Price":
        """Returns a new Price representing the difference between two Price values."""
        return Price(self.amount - other.amount)

    def __eq__(self, other: object) -> bool:
        """Checks whether two Price values are equal."""
        if not isinstance(other, Price):
            return NotImplemented
        return self.amount == other.amount

    def __lt__(self, other: "Price") -> bool:
        """Checks whether this Price is less than another Price."""
        return self.amount < other.amount

    def __gt__(self, other: "Price") -> bool:
        """Checks whether this Price is greater than another Price."""
        return self.amount > other.amount

    def __repr__(self) -> str:
        """Returns a string representation of the Price with two decimal places."""
        return f"{self.amount:.2f}"
