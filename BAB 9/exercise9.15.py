#Lottery Analysis

import random

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'A', 'B', 'C', 'D', 'E']

my_ticket = [3, 7, 'B', 'E']

attempts = 0
while True:
    winning_ticket = random.sample(lottery_items, 4)
    attempts += 1


    if sorted(str(x) for x in my_ticket) == sorted(str(x) for x in winning_ticket):
        print(f"We won after {attempts} attempts!")
        print(f"Winning ticket: {winning_ticket}")
        break


    if attempts >= 1_000_000:
        print(f"Gave up after {attempts:,} attempts. The odds are very slim!")
        break
