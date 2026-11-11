#Silent Cats and Dogs

with open("cats.txt", "w") as f:
    f.write("Whiskers\nFluffy\nShadow\n")

with open("dogs.txt", "w") as f:
    f.write("Buddy\nMax\nBella\n")

filenames = ["cats.txt", "dogs.txt", "birds.txt"] 

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
        print(f"Contents of {filename}:")
        print(contents)
    except FileNotFoundError:
        pass  
