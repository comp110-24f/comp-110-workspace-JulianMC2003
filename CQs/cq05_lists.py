"""Mutating functions."""

__author__ = "730822380"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], mutate: int) -> None:
    a.append(mutate)


def double(name: list[int]) -> None:
    multiply: int = 2
    index: int = 0
    while index < len(name):
        name[index] = name[index] * multiply
        index += 1


double(list_2)
print(list_1)
print(list_2)
