import os
import csv
from typing import List, Iterator, TypedDict
from PIL import Image



class ImageMetadata(TypedDict):
    """Structure describing image metadata."""
    filename: str
    format: str | None
    width: int
    height: int


class ImageMetadataIterator(Iterator[ImageMetadata]):
    """
    Iterator over image files in a directory that yields metadata for each valid image.
    """

    def __init__(self, folder1: str) -> None:
        self.folder: str = folder1
        self.files: List[str] = [
            f for f in os.listdir(folder1)
            if os.path.isfile(os.path.join(folder1, f))
        ]
        self.index: int = 0

    def __iter__(self) -> Iterator[ImageMetadata]:
        """Return the iterator itself."""
        return self

    def __next__(self) -> ImageMetadata:
        """
        Return metadata for the next valid image.
        """
        while self.index < len(self.files):
            filename: str = self.files[self.index]
            self.index += 1
            filepath: str = os.path.join(self.folder, filename)

            try:
                with Image.open(filepath) as img:
                    return {
                        "filename": filename,
                        "format": img.format,
                        "width": img.width,
                        "height": img.height,
                    }
            except (OSError, IOError):
                continue

        raise StopIteration


folder: str = "images"
output_csv: str = "image_metadata.csv"

with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames: List[str] = ["filename", "format", "width", "height"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for meta in ImageMetadataIterator(folder):
        writer.writerow(meta)

print(f"Statistics saved to {output_csv}")
