# Archived Messages

def send_messages(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop(0))

messages = ["Halo", "Apa kabar?", "Semangat belajar Python!"]
archived_messages = []
send_messages(messages[:], archived_messages)
print("Daftar asli:", messages)
print("Pesan arsip:", archived_messages)
