#  Printing Models

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current = unprinted_designs.pop()
        print(f"Mencetak model: {current}")
        completed_models.append(current)

def show_completed_models(completed_models):
    print("Model yang telah dicetak:")
    for model in completed_models:
        print(model)

designs = ["phone case", "robot pendant", "dodecahedron"]
completed = []
print_models(designs[:], completed)
show_completed_models(completed)
