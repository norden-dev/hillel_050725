import zipfile
from pathlib import Path
from types import TracebackType
from typing import Optional, Type, Union


class ZipArchiver:
    """
    A context manager for creating and writing files into a ZIP archive.
    """

    def __init__(
            self,
            zip_path: Union[str, Path],
            mode: str = "w",
            compression: int = zipfile.ZIP_DEFLATED,
    ) -> None:
        """
        Initialize the ZIP archiver.
        """
        self.zip_path = zip_path
        self.mode = mode
        self.compression = compression
        self._zip = None

    def __enter__(self) -> "ZipArchiver":
        """
        Open the ZIP archive.
        """
        self._zip = zipfile.ZipFile(self.zip_path, mode=self.mode, compression=self.compression)
        return self

    def add(self, file_path: Union[str, Path], arcname: Optional[str] = None) -> None:
        """
        Add a file into the archive.
        """
        if self._zip is None:
            raise RuntimeError("Archive is not open. Use this method inside a 'with' block.")

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if arcname is None:
            arcname = path.name

        self._zip.write(path, arcname=arcname)

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> bool:
        """
        Close the ZIP archive.
        """
        if self._zip is not None:
            self._zip.close()

        return False


with ZipArchiver("data_backup.zip") as arch:
    arch.add("important.txt")
    arch.add("report.pdf")
    arch.add("photo.png", arcname="images/photo.png")
