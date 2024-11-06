__author__ = "730822380"


def all(list1: list[int], deciding_factor: int) -> bool:
    idx: int = 0
    condition: bool = True
    if len(list1) == 0:
        condition = False
    while idx < len(list1):
        if deciding_factor != list1[idx]:
            condition = False
        idx += 1
    return condition


# uses the while loops and idx to determine if the "deciding_factor"
# is seen in all parts of the list.


def max(input: list[int]) -> int:
    idx: int = 0
    largest_num: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while idx < len(input):
        if input[idx] > largest_num:
            largest_num = input[idx]
        idx += 1
    return largest_num


# uses the while loop and idx to find the largest number in a list.


def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx: int = 0
    condition: bool = True
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return condition


# how can i make this work while also making sure that
# the length of each of the lists are the same?

# set the condition to true and then check to see if there are any
# false properties.


def extend(list_a: list[int], list_b: list[int]) -> None:
    idx: int = 0
    while idx < len(list_b):
        list_a.append(list_b[idx])
        idx += 1

