#Guest

name = "Alice Wonderland"
print(f"Please enter your name: {name}")

with open("guest.txt", "w") as f:
    f.write(name)

print(f"Name '{name}' has been saved to guest.txt.")
