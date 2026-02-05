from typing import Generator


def even_numbers(start: int = 2) -> Generator[int, None, None]:
    """
    Generate an infinite sequence of even numbers.

    """
    n = start
    while True:
        yield n
        n += 2


def save_first_n_even_numbers(output_path: str, count: int = 100, start: int = 2) -> None:
    """
    Generate and save the first N even numbers into a text file.

    """
    gen = even_numbers(start=start)

    with open(output_path, "w", encoding="utf-8") as file:
        for _ in range(count):
            file.write(str(next(gen)) + "\n")


save_first_n_even_numbers("even_numbers.txt", count=100, start=2)
print("Saved 100 even numbers to even_numbers.txt")
