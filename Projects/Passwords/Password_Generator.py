"""This code is used to create a password for the user."""

import random


def rand_number() -> str:
    pass_length: int = int(
        input(
            "Please Select the Length of Your Password (Between 10 and 30 Characters): "
        )
    )
    # why does python make the parenthesis go to new lines?
    idx: int = 1
    password: str = ""
    print(f"Password Length: {pass_length}")
    while pass_length > 30 or pass_length < 10:
        pass_length = int(
            input("Please choose a length between 10 and 30 characters: ")
        )
    while idx <= pass_length:
        password += chr(random.randint(32, 122))
        idx += 1
    print("Please copy and paste this password to a safe location.")
    return password


print(rand_number())
