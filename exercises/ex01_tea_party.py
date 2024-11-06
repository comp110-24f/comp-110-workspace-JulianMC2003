"""EX01 Date: 08/29/24"""

__author__: str = "730822380"


def main_planner(guests: int) -> None:
    """Will give the details of the entire party."""
    """Will need to make guests act as people."""
    """Make tea bags and treats act as the tea and treat counts"""
    """Code should replace people with guests and counts with tea bags and treats"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Total # of people * 2 for total # of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """Total # of people * 1.5 for total # of treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost for tea and treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
