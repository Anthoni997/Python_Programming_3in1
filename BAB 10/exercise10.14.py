#Verify User

import json

filename = "username.json"


def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(filename):
    """Prompt for a new username and store it."""

    username = "alice_wonder"  # Simulated
    print(f"What is your username? {username}")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name, with verification."""
    username = get_stored_username(filename)
    if username:
        
        confirm = "yes"  
        print(f"Are you {username}? (yes/no): {confirm}")

        if confirm.lower() == "yes":
            print(f"Welcome back, {username}!")
        else:
            
            username = get_new_username(filename)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you when you come back, {username}!")



with open(filename, "w") as f:
    json.dump("alice_wonder", f)

greet_user()
