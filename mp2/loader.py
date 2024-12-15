import random
from pathlib import Path

file_path = "./static/mp2dataset.txt"


def read_data() -> "list[int]":
    """Read the integers from the provided dataset into an array."""
    try:
        with Path(file_path).open() as file:
            return [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return []
    except ValueError:
        print("Error: The file contains non-integer values.")
        return []


def query_data(count: int) -> "list[int]":
    """Query N random integers from the provided dataset into an arary."""
    data = read_data()
    return [random.choice(data) for _ in range(count)]  # noqa: S311
