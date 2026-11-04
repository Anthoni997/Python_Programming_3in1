#Seeing the World

places = ["Tokyo", "Paris", "Cairo", "New York", "Sydney", "Rome"]

print("Original order:")
print(places)

print("\nAlphabetical order (sorted):")
print(sorted(places))

print("\nStill original order:")
print(places)

print("\nReverse alphabetical order (sorted with reverse=True):")
print(sorted(places, reverse=True))

print("\nStill original order:")
print(places)

places.reverse()
print("\nAfter reverse():")
print(places)

places.reverse()
print("\nBack to original after second reverse():")
print(places)

places.sort()
print("\nAfter sort() - permanent alphabetical:")
print(places)

places.sort(reverse=True)
print("\nAfter sort(reverse=True) - permanent reverse alphabetical:")
print(places)