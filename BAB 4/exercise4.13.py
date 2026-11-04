#Buffet

buffet_foods = ("rice", "chicken", "salad", "soup", "bread")

print("The restaurant offers:")
for food in buffet_foods:
    print(f"  - {food}")

print("\nTrying to modify a tuple item...")
try:
    buffet_foods[0] = "pasta"
except TypeError as e:
    print(f"  Error: {e}")
    print("  Tuples are immutable - items cannot be changed!")

buffet_foods = ("pasta", "chicken", "salad", "soup", "cake")
print("\nRevised menu:")
for food in buffet_foods:
    print(f"  - {food}")