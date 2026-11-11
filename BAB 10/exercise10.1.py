#Learning Python

filename = "learning_python.txt"

with open(filename, "w") as f:
    f.write("In Python you can store information in variables.\n")
    f.write("In Python you can organize data using lists and dictionaries.\n")
    f.write("In Python you can automate tasks using loops and functions.\n")
    f.write("In Python you can create reusable blueprints using classes.\n")
    f.write("In Python you can read and write files easily.\n")

print("Contents of learning_python.txt:")
print("-" * 40)
with open(filename) as f:
    contents = f.read()
print(contents)
