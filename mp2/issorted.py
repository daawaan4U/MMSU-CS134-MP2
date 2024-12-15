def issorted(arr: "list[int]") -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
