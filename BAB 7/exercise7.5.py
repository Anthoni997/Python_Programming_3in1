#Movie Tickets

while True:
    age_text = input("Masukkan usia (ketik 'quit' untuk selesai): ")
    if age_text.lower() == "quit":
        break
    age = int(age_text)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"Harga tiket: ${price}")
