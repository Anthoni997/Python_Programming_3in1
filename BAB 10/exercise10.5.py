#Guest Book

simulated_names = ["Alice", "Bob", "Charlie", "Diana", "quit"]
names = []

for name in simulated_names:
    print(f"Enter your name (or 'quit' to stop): {name}")
    if name.lower() == "quit":
        break
    names.append(name)
    print(f"Hello, {name}! Your name has been added to the guest book.\n")

# Write all names to guest_book.txt
with open("guest_book.txt", "w") as f:
    for name in names:
        f.write(f"{name}\n")

print("\nGuest book saved. Contents of guest_book.txt:")
with open("guest_book.txt") as f:
    print(f.read())
