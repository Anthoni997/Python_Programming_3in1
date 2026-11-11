#Addition Calculator

print("Addition Calculator (type 'quit' to exit)")
simulated_inputs = [("5", "3"), ("10", "abc"), ("7", "13"), ("quit", "")]

for first, second in simulated_inputs:
    print(f"\nFirst number: {first}")
    if first.lower() == "quit":
        print("Exiting calculator.")
        break
    print(f"Second number: {second}")
    if second.lower() == "quit":
        print("Exiting calculator.")
        break
    try:
        total = int(first) + int(second)
    except ValueError:
        print("Error: Please enter valid numbers only!")
    else:
        print(f"Result: {first} + {second} = {total}")
