__authnor__ = "730822380"


def only_evens(lista: list[int]) -> list[int]:
    evens = []
    for num in lista:
        if num % 2 == 0:
            evens.append(num)
    return evens


# takes list and adds even numbers to a new list and returns them


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    if len(input_list) == 0 or start >= len(input_list) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(input_list):
        end = len(input_list)
    return input_list[start:end]


# Takes list and returns the numbers between two index


def add_at_index(list1, element, idx) -> None:
    if idx < 0 or idx > len(list1):
        raise IndexError("Index is out of range.")
    new_list = []
    for i in range(len(list1)):
        if i == idx:
            new_list.append(element)
        new_list.append(list1[i])
    if idx == len(list1):
        new_list.append(element)
    list1 = new_list


# shifts numbers over and adds element into the index
