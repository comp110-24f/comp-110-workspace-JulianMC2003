__author__ = "730822380"

def invert(before: dict[str,str]) -> dict[str,str]:
    keys: list[str] = []
    values: list[str ]= []
    idx1: int = 0
    idx2: int = 0
    new: dict[str,str] = {}
    for i in before:
        keys.append(i)
        values.append(before[i])
    while idx1 < len(keys):
        while idx2 < len(keys):
            if idx1 != idx2:
                if keys[idx1] == keys[idx2]:
                    raise KeyError(f"Duplicate found: {keys[idx1]}")
            idx2 += 1
        idx2 = 0
        idx1 +=1
    idx1 = 0
    while idx1 < len(values):
        new[values[idx1]] = keys[idx1]
        idx1 += 1
    return new

#how can i obtain the keys without using .items()?
    #by using for in loops to otain the values

def favorite_color(colors: dict[str,str]) -> str:
    values: list[str] = []
    idx1: int = 0
    idx2: int = 0
    counter: int = 1
    favorite: str = ""
    favorite_counter: int = 0
    for i in colors:
        values.append(colors[i])
    while idx1 < len(values):
        while idx2 < len(values):
            if idx1 != idx2:
                if values[idx1] == values[idx2]:
                    counter += 1
            idx2 += 1
        if counter > favorite_counter:
            favorite_counter = counter
            favorite = values[idx1]
        counter = 1
        idx2 = 0
        idx1 += 1
    return favorite

# uses idxs and for in loops to distinguish what a persons favorite color is and tracks how many times it is common with others

def count(main:list[str]) -> dict[str,int]:
    main_dict: dict[str, int] = {}
    for i in main:
        if i in main_dict:
            main_dict[i] += 1
        else: 
            main_dict[i] = 1
    return main_dict

# decided to switch for in loops

# uses the in function in order to check dict to see if the key is there already

def alphabetizer(main:list[str]) -> dict[str,int]:
    main_dict: dict[str, int] = {}
    for i in main:
        first_letter = i[0].lower()
        if first_letter not in main_dict:
            main_dict[first_letter] = []
        main_dict[first_letter].append(i)
    return main_dict

# uses the .lower function to turn capital letters into lower case letters

# can alphabetize each item in a list according to what the first letter is

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
    return None

# this was nice and simple)

    
                
    
