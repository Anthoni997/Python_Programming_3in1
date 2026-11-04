#Rivers

rivers = {"nile": "egypt", "amazon": "brazil", "kapuas": "indonesia"}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("Sungai:", list(rivers.keys()))
print("Negara:", list(rivers.values()))
