#Favorite Number Remembered.

import json

filename = "favorite_number.json"


def get_stored_number(filename):
    """Get stored favorite number if available."""
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number(filename):
    """Prompt for a new favorite number and store it."""
   
    number = "42"  
    print(f"What is your favorite number? {number}")
    with open(filename, "w") as f:
        json.dump(number, f)
    return number


def remember_number():
    """Remember a favorite number, between sessions."""
    number = get_stored_number(filename)
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = get_new_number(filename)
        print(f"We'll remember your favorite number: {number}.")


remember_number()
