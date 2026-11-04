#Sending Messages

def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop(0)
        print(current)
        sent_messages.append(current)

messages = ["Halo", "Apa kabar?", "Semangat belajar Python!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Daftar asli:", messages)
print("Pesan terkirim:", sent_messages)
