#Simpler Code

filename = "learning_python.txt"
with open(filename, "w") as f:
    f.write("In Python you can store information in variables.\n")
    f.write("In Python you can organize data using lists and dictionaries.\n")
    f.write("In Python you can automate tasks using loops and functions.\n")

print("Reading file directly (no temp variable):")
print("-" * 40)
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
