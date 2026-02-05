import os
from typing import Iterator


class ReverseFileIterator:
    """
    An iterator that reads a text file in reverse order, yielding lines
    from the end of the file to the beginning without loading the entire
    file into memory.

    """

    def __init__(self, file_path: str,encoding: str = "utf-8",chunk_size: int = 4096,) -> None:

        self.file_path = file_path
        self.encoding = encoding
        self.chunk_size = chunk_size

    def __iter__(self) -> Iterator[str]:
        """
        Iterate over the file lines in reverse order.
        """
        with open(self.file_path, "rb") as f:
            f.seek(0, os.SEEK_END)
            file_size: int = f.tell()
            buffer: bytes = b""
            position: int = file_size

            while position > 0:
                read_size: int = min(self.chunk_size, position)
                position -= read_size
                f.seek(position)
                chunk: bytes = f.read(read_size)

                buffer = chunk + buffer
                lines = buffer.split(b"\n")

                buffer = lines[0]

                for line in reversed(lines[1:]):
                    yield line.decode(self.encoding)

            if buffer:
                yield buffer.decode(self.encoding)


for line in ReverseFileIterator("example.log"):
    print(line)
