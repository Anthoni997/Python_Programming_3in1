#Favorite Places

favorite_places = {
    "andi": ["bali", "jogja"],
    "budi": ["bandung"],
    "citra": ["raja ampat", "bromo", "malang"]
}
for name, places in favorite_places.items():
    print(f"Tempat favorit {name.title()}:")
    for place in places:
        print("-", place.title())
