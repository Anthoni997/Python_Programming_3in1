#Python Module of the Week

import random

print("random.random():", random.random())

print("random.randint(1, 10):", random.randint(1, 10))

colors = ["red", "green", "blue", "yellow", "purple"]
print("random.choice(colors):", random.choice(colors))

deck = list(range(1, 14))
random.shuffle(deck)
print("Shuffled deck:", deck)

sample = random.sample(range(100), 5)
print("random.sample(range(100), 5):", sample)

random.seed(42)
print("Seeded random (42):", random.randint(1, 100))
