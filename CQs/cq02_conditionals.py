__author__: str = "730822380"

import random


def guess_a_number() -> None:
    x: int = int(input("Guess a number:"))
    secret: int = random.randint(0, 1)
    print("Your guess was " + str(x))

    if int(x) == secret:
        print("You got it!")
    if int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    if int(x) > secret:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
