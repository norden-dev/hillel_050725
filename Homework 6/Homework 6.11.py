from typing import Iterator


def incremental_average(file_path) -> Iterator[float]:
    """ Reads a large file line by line and yields the updated average after each number."""
    total = 0.0
    count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            value = float(line)
            total += value
            count += 1

            yield total / count


for avg in incremental_average("data.txt"):
    print(avg)
