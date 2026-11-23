# import random

# # number = random.randint(1, 10)
# # print(number)

import random 
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for i in cards:
    print(i)