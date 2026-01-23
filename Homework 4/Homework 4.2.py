class EmptyLineError(Exception):
    """ Exception raised when a file is empty or contains only whitespace."""
    pass


def file_average(file_name: str) -> None:
    """Reads numbers from a text file and calculates their arithmetic average"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

        tokens = content.split()

        if not tokens:
            raise EmptyLineError("File is empty or contains only whitespace.")

        numbers = []
        for token in tokens:
            try:
                numbers.append(float(token))
            except ValueError:
                raise ValueError(f"Non-numeric data found: '{token}'")

        average = sum(numbers) / len(numbers)
        print(f"Average value: {average}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except EmptyLineError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
