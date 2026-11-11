#Lottery

import random

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'A', 'B', 'C', 'D', 'E']

winning_ticket = random.sample(lottery_items, 4)
print("Today's winning lottery numbers/letters:")
print(winning_ticket)
print("\nAny ticket matching these 4 items wins a prize!")
