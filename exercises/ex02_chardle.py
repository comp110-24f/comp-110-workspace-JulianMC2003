"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730833380"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    x: str = input("Enter a 5-character word: ")
    if len(x) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        # how do i fix the int is not scriptable.
        # i needed to change len[x] to len(x).
    return x


def input_letter() -> str:
    y: str = input("Enter a single character: ")
    if len(y) != 1:
        print("Error: Character must be a single character.")
        exit()
    return y


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    index: int = 0
    counter: int = 0
    while index < 5:
        if letter == word[index]:
            print(letter + " found at index " + str(index))
            counter = counter + 1
        index = index + 1
    if counter == 0:
        print("No instances of " + letter + " found in " + word)
    if counter == 1:
        print(str(counter) + " instance of " + letter + " found in " + word)
    if counter > 1:
        print(str(counter) + " instances of " + letter + " found in " + word)


# infinite loops what do I do?
# set index as my condition instead of using a bool to stop the loops.

if __name__ == "__main__":
    main()

# my program is running twice, what shoud I do?
