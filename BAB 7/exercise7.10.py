#Dream Vacation

responses = {}
while True:
    name = input("Nama Anda: ")
    place = input("Tempat liburan impian: ")
    responses[name] = place
    repeat = input("Apakah orang lain ingin menjawab? (yes/no): ")
    if repeat.lower() == "no":
        break
print("\n--- Hasil Polling ---")
for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")
