import random

from mp2.issorted import issorted


def stupidsort(data: "list[int]") -> "list[int]":
    data = data.copy()
    while not issorted(data):
        random.shuffle(data)
    return data
