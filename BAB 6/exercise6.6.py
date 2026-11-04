#Polling

favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}
people = ["jen", "sarah", "mike", "phil", "anna"]
for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} telah mengikuti polling.")
    else:
        print(f"{person.title()}, silakan ikuti polling.")
