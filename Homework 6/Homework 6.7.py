from typing import Iterator


def error_line_generator(log_path: str) -> Iterator[str]:
    """
    Yields only lines with HTTP status 4XX or 5XX from a large log file.
    """
    with open(log_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            if len(parts) > 8:
                status_code = parts[8]

                if status_code.startswith(("4", "5")):
                    yield line


def write_errors_to_file(log_path: str, output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as out_file:
        for error_line in error_line_generator(log_path):
            out_file.write(error_line)


log_file = "access.log"
errors_file = "errors.log"

write_errors_to_file(log_file, errors_file)
print("Помилки записані у файл errors.log")
