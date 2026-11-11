# Exercise 10-13: User Dictionary

import json

filename = "user_data.json"


def get_user_info():
    """Collect user information and store it."""
    
    username = "alice_wonder"
    age = "25"
    city = "Jakarta"
    print(f"Enter your username: {username}")
    print(f"Enter your age: {age}")
    print(f"Enter your city: {city}")

    user_data = {
        "username": username,
        "age": age,
        "city": city,
    }

    with open(filename, "w") as f:
        json.dump(user_data, f)

    return user_data


def load_user_info():
    """Load and display saved user information."""
    try:
        with open(filename) as f:
            user_data = json.load(f)
    except FileNotFoundError:
        print("No user data found. Please enter your info.")
        user_data = get_user_info()

    print("\n--- Remembered User Information ---")
    print(f"  Username : {user_data['username']}")
    print(f"  Age      : {user_data['age']}")
    print(f"  City     : {user_data['city']}")


get_user_info()

load_user_info()
