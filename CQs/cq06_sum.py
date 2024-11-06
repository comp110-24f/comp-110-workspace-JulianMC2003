"""Summing the elements of a list using different loops"""

__author__ = "730822380"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    answer: float = 0.0
    while idx < len(vals):
        answer = answer + vals[idx]
        idx += 1
    return answer


def f_sum(vals: list[float]) -> float:
    answer: float = 0.0
    for num in vals:
        answer = answer + num
    return answer


def f_range_sum(vals: list[float]) -> float:
    answer: float = 0.0
    for num in range(0, len(vals)):
        answer = answer + vals[num]
    return answer
