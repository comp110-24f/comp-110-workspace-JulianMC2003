__author__ = "730822380"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False
    while turn <= 6 and not win:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        print(result)
        if guess == secret:
            win = True
        if win:
            print(f"You won in {turn}/6 turns!")
        turn += 1
    if not win:
        print("X/6 - Sorry, try again tomorrow!")


# this part took so long
# printing twice what do i do
# take out unessesary print

def input_guess(secret_word_len: int) -> str:
    word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} characters! Try again: ")
    return word


# use f-string instead of using str(secret_word_len)


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Will search the secret_word for the char used in char_guess"""
    """If char is in secret word, will return a true bool"""
    index: int = 0
    condition: bool = False
    x: int = 0
    assert len(char_guess) == 1
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            x += 1
        index += 1
    if x > 0:
        condition = True
    return condition


# x will act as a way to see if there are any chars in the secret word


def emojified(guess: str, secret: str) -> str:
    """This function will compare the values of the guess and the secret"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""
    assert len(guess) == len(secret)
    while index < len(secret):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]) is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


# this one actually was much easier than anticipated

if __name__ == "__main__":
    main(secret="MOCHA")
