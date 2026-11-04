#More Guests

guests = ["Isaac Newton", "Marie Curie", "Leonardo da Vinci"]
print("We found a bigger table! We can invite more guests.\n")
guests.insert(0, "Nikola Tesla")
guests.insert(2, "Stephen Hawking")
guests.append("Ada Lovelace")
print("Updated invitation list:")
for guest in guests:
    print(f"Dear {guest}, I would love to have you over for dinner!")