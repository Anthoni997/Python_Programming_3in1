#Learning C

filename = "learning_python.txt"
with open(filename, "w") as f:
    f.write("In Python you can store information in variables.\n")
    f.write("In Python you can organize data using lists and dictionaries.\n")
    f.write("In Python you can automate tasks using loops and functions.\n")
    f.write("In Python you can create reusable blueprints using classes.\n")
    f.write("In Python you can read and write files easily.\n")

print("Modified lines (Python -> C):")
print("-" * 40)
with open(filename) as f:
    for line in f:
        print(line.replace("Python", "C"), end="")
