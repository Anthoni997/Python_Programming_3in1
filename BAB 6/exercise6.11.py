#Cities

cities = {
    "surakarta": {"country": "indonesia", "population": 500000, "fact": "Kota budaya."},
    "tokyo": {"country": "japan", "population": 14000000, "fact": "Memiliki sistem transportasi luas."},
    "paris": {"country": "france", "population": 2100000, "fact": "Dikenal dengan Menara Eiffel."}
}
for city, info in cities.items():
    print(f"\nKota: {city.title()}")
    print(f"Negara: {info['country'].title()}")
    print(f"Populasi: {info['population']:,}")
    print(f"Fakta: {info['fact']}")
