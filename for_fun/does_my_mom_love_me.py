import random


def does_my_mom_love_me() -> None:
    x = random.randint(0, 1)
    if x == 0:
        print("Yes")
    if x == 1:
        print("No")


does_my_mom_love_me()
