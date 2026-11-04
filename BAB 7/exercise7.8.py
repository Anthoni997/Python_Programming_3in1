#Deli

sandwich_orders = ["tuna", "pastrami", "chicken"]
finished_sandwiches = []
while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"Saya membuat sandwich {current}.")
    finished_sandwiches.append(current)
print("Sandwich selesai:", finished_sandwiches)
