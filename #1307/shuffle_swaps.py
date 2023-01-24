import random


def shuffle_deck(deck, rand_int):
    n = len(deck)
    for i in range(n - 1):
        # Generate a random index between i and n-1
        j = rand_int(i, n-1)
        # Swap the card at index i with the randomly selected card
        deck[i], deck[j] = deck[j], deck[i]
    return deck


if __name__ == "__main__":
    deck = list(range(52))
    print(shuffle_deck(deck, random.randint))
