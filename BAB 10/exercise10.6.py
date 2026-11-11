#Addition

print("--- Simulation 1: Valid numbers ---")
try:
    first_number = int("5")
    second_number = int("3")
    print(f"First number: {first_number}")
    print(f"Second number: {second_number}")
except ValueError:
    print("Error: Please enter valid numbers only!")
else:
    total = first_number + second_number
    print(f"{first_number} + {second_number} = {total}")

print("\n--- Simulation 2: Invalid input (text) ---")
try:
    first_number = int("5")
    second_number = int("abc")  # Will raise ValueError
    print(f"First number: {first_number}")
    print(f"Second number: {second_number}")
except ValueError:
    print("Error: Please enter valid numbers only!")
else:
    total = first_number + second_number
    print(f"{first_number} + {second_number} = {total}")
