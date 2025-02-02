import random

suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []

# Make a deck of cards
for suit in suits:
    for value in values:
        deck.append(f"{value}{suit}")

# Shuffle your `deck` and print it out
random.shuffle(deck)
print("Shuffled deck:", deck)

# Sample a hand of 5 cards and print it out (WITHOUT replacement)
hand = random.sample(deck, 5)
print("Sampled hand:", hand)