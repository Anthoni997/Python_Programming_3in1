#Code Review

# --- PEP 8 version of Exercise 4-1 (Pizzas) ---
pizzas = ["pepperoni", "margherita", "barbecue chicken"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!\n")

# --- PEP 8 version of Exercise 4-6 (Odd Numbers) ---
odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)
print()

# --- PEP 8 version of Exercise 4-9 (Cube Comprehension) ---
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)