#Shrinking Guest List

guests = ["Nikola Tesla", "Isaac Newton", "Stephen Hawking",
          "Marie Curie", "Leonardo da Vinci", "Ada Lovelace"]
print("I can only invite two people to dinner.\n")
# Remove guests until only 2 remain
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry, {removed}, I can't invite you to dinner.")
# Print final invitations for the 2 remaining
print(f"\nDear {guests[0]}, you are still invited to dinner!")
print(f"Dear {guests[1]}, you are still invited to dinner!")
# Remove the last two names
del guests[0]
del guests[0]
print(f"\nFinal guest list: {guests}")