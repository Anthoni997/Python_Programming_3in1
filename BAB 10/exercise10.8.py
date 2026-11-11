# Cats and Dogs

with open("cats.txt", "w") as f:
    f.write("Whiskers\nFluffly\nShadow\n")

with open("dogs.txt", "w") as f:
    f.write("Buddy\nMax\nBella\n")

filenames = ["cats.txt", "dogs.txt", "birds.txt"]  # birds.txt doesn't exist

for filename in filenames:
    print(f"\nReading {filename}:")
    print("-" * 25)
    try:
        with open(filename) as f:
            contents = f.read()
        print(contents)
    except FileNotFoundError:
        print(f"  Sorry, the file '{filename}' does not exist.")
