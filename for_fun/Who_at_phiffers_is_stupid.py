import random


def stupid_person_at_phiffers() -> str:
    x = "somebody"
    person = random.randint(0, 9)
    if person == 0:
        x = "Josh"
    if person == 1:
        x = "Bailey"
    if person == 2:
        x = "Kayce Jo"
    if person == 3:
        x = "Matthew"
    if person == 4:
        x = "Henry"
    if person == 5:
        x = "Kassie"
    if person == 6:
        x = "Lainey"
    if person == 7:
        x = "Jaylen"
    if person == 8:
        x = "Jay"
    if person == 9:
        x = "Julian, but he doesnt work there anymore"
    return str(x)


print("The stupid person is " + str(stupid_person_at_phiffers()))
