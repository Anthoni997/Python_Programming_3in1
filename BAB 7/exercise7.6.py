#Three Exits

# Versi 1: kondisi while.
active = True
while active:
    answer = input("Ketik 'stop' untuk berhenti: ")
    if answer.lower() == "stop":
        active = False
    else:
        print("Program masih berjalan.")

# Versi 2: active variable.
active = True
while active:
    topping = input("Masukkan topping (quit untuk selesai): ")
    if topping.lower() == "quit":
        active = False
    else:
        print(f"Menambahkan {topping}.")

# Versi 3: break.
while True:
    answer = input("Ketik 'quit' untuk keluar: ")
    if answer.lower() == "quit":
        break
    print("Anda mengetik:", answer)
