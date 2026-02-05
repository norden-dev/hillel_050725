import uuid
from typing import Iterator


class UUIDIterator(Iterator[str]):
    """
    An infinite iterator that generates random UUID4 values.
    """

    def __iter__(self) -> "UUIDIterator":
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self) -> str:
        """
        Generate and return the next UUID4 hex string.
        """
        return uuid.uuid4().hex


id1: UUIDIterator = UUIDIterator()

for _ in range(3):
    print(next(id1))
