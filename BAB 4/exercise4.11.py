#My Pizzas, Your Pizzas

my_pizzas = ["pepperoni", "margherita", "barbecue chicken"]
friend_pizzas = my_pizzas[:]  # Make a copy

my_pizzas.append("four cheese")
friend_pizzas.append("veggie supreme")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"  - {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"  - {pizza}")