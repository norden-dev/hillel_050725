from typing import Optional


class BinaryBlockReader:
    """
    Context manager for reading a binary file in fixed-size blocks.
    """

    def __init__(self, file_path: str, block_size: int = 1024) -> None:

        self.file_path = file_path
        self.block_size = block_size
        self._file: Optional[object] = None

    def __enter__(self) -> "BinaryBlockReader":
        self._file = open(self.file_path, "rb")
        return self

    def read_blocks(self):
        """
        Generator that yields blocks of bytes.
        """
        if self._file is None:
            raise RuntimeError("File is not open. Use inside a 'with' block.")

        while True:
            block = self._file.read(self.block_size)
            if not block:
                break
            yield block

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._file is not None:
            self._file.close()
        return False


total_bytes = 0

with BinaryBlockReader("bigfile.bin", block_size=1024) as reader:
    for chunk in reader.read_blocks():
        total_bytes += len(chunk)

print("Read bytes:", total_bytes)
