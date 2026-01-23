class InsufficientFundsException(Exception):
    """Exception raised when there are not enough funds to complete a transaction."""

    def __init__(
            self,
            required_amount: float,
            current_balance: float,
            currency: str,
            transaction_type: str
    ) -> None:
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

        super().__init__(self.__str__())

    def __str__(self) -> str:
        return (
            f"Insufficient funds for {self.transaction_type}: "
            f"required {self.required_amount} {self.currency}, "
            f"available {self.current_balance} {self.currency}"
        )


class BankAccount:
    """Represents a simple bank account."""

    def __init__(self, balance: float, currency: str) -> None:
        self.balance = balance
        self.currency = currency

    def withdrawal(self, amount: float) -> None:
        """Withdraw money from the account."""
        if self.balance < amount:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="withdrawal"
            )

        self.balance -= amount
        print(f"Withdrawal successful. Balance: {self.balance} {self.currency}")

    def purchase(self, amount: float) -> None:
        """Make a purchase using the account balance."""
        if self.balance < amount:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="purchase"
            )

        self.balance -= amount
        print(f"Purchase successful. Balance: {self.balance} {self.currency}")


account = BankAccount(100.0, "USD")

try:
    account.withdrawal(50)
    account.purchase(100)
except InsufficientFundsException as e:
    print(e)
