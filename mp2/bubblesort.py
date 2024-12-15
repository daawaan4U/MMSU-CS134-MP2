def bubblesort(data: "list[int]") -> "list[int]":
    data = data.copy()
    n = len(data)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break

    return data
