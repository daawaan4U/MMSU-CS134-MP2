def partition(arr: "list[int]", low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(data: "list[int]") -> "list[int]":
    data = data.copy()

    stack = [(0, len(data) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot_index = partition(data, start, end)
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return data
