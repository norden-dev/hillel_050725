from pathlib import Path
from typing import Iterator, Tuple


class DirectoryFilesIterator:
    """
    Iterable that yields all files in a given directory one by one.
    """

    def __init__(self, directory: str):
        self.directory = Path(directory)

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        for item in self.directory.iterdir():
            if item.is_file():
                yield item.name, item.stat().st_size


directory_path = "."

files = DirectoryFilesIterator(directory_path)

for name, size in files:
    print(f"Файл: {name}, Розмір: {size} байт")
