#No Pastrami

sandwich_orders = ["pastrami", "tuna", "pastrami", "chicken", "pastrami"]
print("Deli kehabisan pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("Pesanan tersisa:", sandwich_orders)
