#Favorite Number

import json

favorite_number = "7"  # Simulated input
print(f"What is your favorite number? {favorite_number}")

filename = "favorite_number.json"
with open(filename, "w") as f:
    json.dump(favorite_number, f)

print(f"Your favorite number has been saved to {filename}.")

print("\n--- Reading back the saved number ---")
with open(filename) as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")
