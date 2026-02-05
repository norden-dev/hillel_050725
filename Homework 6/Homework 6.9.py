import os
import shutil
import tempfile


class SafeFileUpdate:
    """
    A context manager that safely updates a file using a backup and a temporary file.
    """

    def __init__(self, filepath: str) -> None:
        """
        Initialize the context manager.
        """
        self.filepath = filepath
        self.backup_path = filepath + ".bak"
        self.temp_path = None

    def __enter__(self) -> str:
        """
        Create a backup (if needed) and a temporary file for writing new content.
        """
        if os.path.exists(self.filepath):
            shutil.copy2(self.filepath, self.backup_path)  # type: ignore[arg-type]
        else:
            self.backup_path = None

        fd, self.temp_path = tempfile.mkstemp(prefix="tmp_", suffix=".txt")
        os.close(fd)

        return self.temp_path

    def __exit__(
            self,
            exc_type,
            exc_val,
            exc_tb,
    ) -> bool:
        """
        Finalize the update.
        """
        if exc_type is not None:
            if self.backup_path and os.path.exists(self.backup_path):
                shutil.copy2(self.backup_path, self.filepath)

            if self.temp_path and os.path.exists(self.temp_path):
                os.remove(self.temp_path)

            return False

        if self.temp_path is not None:
            shutil.move(self.temp_path, self.filepath)

        if self.backup_path and os.path.exists(self.backup_path):
            os.remove(self.backup_path)

        return True


with SafeFileUpdate("important.txt") as temp:
    with open(temp, "w", encoding="utf-8") as f:
        f.write("text\n")
