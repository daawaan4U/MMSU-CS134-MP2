import math
import sys
import time

from mp2.bubblesort import bubblesort
from mp2.issorted import issorted
from mp2.loader import query_data
from mp2.quicksort import quicksort
from mp2.stupidsort import stupidsort


def prettytime(ns: int) -> str:
    NS_PER_S = 1_000_000_000  # noqa: N806
    NS_PER_MS = 1_000_000  # noqa: N806

    # Calculate s
    s = math.floor(ns / NS_PER_S)
    ns %= NS_PER_S

    # Calculate millis
    ms = math.floor(ns / NS_PER_MS)
    ns %= NS_PER_MS

    time_str = []
    if s > 0:
        time_str.append(f"{s}s")
    if ms > 0:
        time_str.append(f"{ms}ms")
    time_str.append(f"{ns}ns")

    return " ".join(time_str)


def program() -> None:
    print("Enter sorting algorithm to use: ")
    print(" [1] Quick Sort")
    print(" [2] Bubble Sort")
    print(" [3] Stupid Sort")
    choice = input("--: ")
    if choice == "1":
        sorter = quicksort
    elif choice == "2":
        sorter = bubblesort
    elif choice == "3":
        sorter = stupidsort
    else:
        print("Invalid choice.")
        sys.exit(-1)

    size = int(input("Enter dataset size to use: "))

    trials = int(input("Enter # of trials to run: "))

    elapses: list[int] = []

    for i in range(trials):
        print()
        print(f"--- Trial #{i + 1}/{trials} ---")
        print("Loading data ... ", end="")
        dataset = query_data(size)
        print("✅")

        print("Sorting ... ", end="")
        timestamp_start = time.time_ns()
        sorted = sorter(dataset)  # noqa: A001
        timestamp_end = time.time_ns()
        print("✅" if issorted(sorted) else "❌")

        time_elapsed = timestamp_end - timestamp_start
        elapses.append(time_elapsed)
        running_average = int(sum(elapses) / len(elapses))

        print(
            f"Elapsed: {prettytime(time_elapsed)}, Running Average: {prettytime(running_average)}",  # noqa: E501
        )

    average = int(sum(elapses) / len(elapses))
    print()
    print(f"Average: {prettytime(average)}")
    print("Laps: ")
    for i, elapsed in enumerate(elapses):
        print(f"{i + 1}, {prettytime(elapsed)}")
