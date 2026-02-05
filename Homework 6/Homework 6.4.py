import re


def filter_lines(
        input_path: str,
        keyword: str,
        encoding: str = "utf-8",
        flags: int = re.IGNORECASE
):
    """
    A generator that reads a large text file line by line and yields only
    the lines that match the given regular expression pattern.
    """
    regex = re.compile(keyword, flags)

    with open(input_path, "r", encoding=encoding, errors="ignore") as f:
        for line in f:
            if regex.search(line):
                yield line


def writer_lines(
        input_path: str,
        output_path: str,
        keyword: str,
        encoding: str = "utf-8",
        flags: int = re.IGNORECASE
) -> None:
    """
    Filters lines from the input file using a regex pattern and writes
    matching lines into a new output file.

    """
    with open(output_path, "w", encoding=encoding) as out:
        for line in filter_lines(input_path, keyword, encoding=encoding, flags=flags):
            out.write(line)


input_file = "big_log.txt"
output_file = "filtered_log.txt"

search = r"keyword"

writer_lines(input_file, output_file, search)
