__author__ = "730822380"


def num_instances(phrase: str, search_char: str) -> str:
    instance: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            instance = instance + 1
        index = index + 1
    return str(instance)


print(num_instances(phrase="hello", search_char="l"))
