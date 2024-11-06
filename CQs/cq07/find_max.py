__author__ = "730822380"


def find_and_remove_max(list1: list[int]) -> int:
    if len(list1) == 0:
        return -1
    largest_num: int = list1[0]
    idx: int = 0
    for nums in list1:
        if nums > largest_num:
            largest_num = nums
    while idx < len(list1):
        if list1[idx] == largest_num:
            list1.pop(idx)
        idx += 1
        # print(list1)
    return largest_num


largest_num: int = list1[0]
idx: int = 0
for i in range(len(list1)):
    if list[i] > largest_num:
        largest_num = list[i]
        idx = i

list1.pop(idx)
return largest_num
