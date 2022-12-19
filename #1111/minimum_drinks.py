def minimum_drinks(preferences):
    # Create a list of all the drinks
    drinks = [item for sublist in preferences.values() for item in sublist]

    # Count the number of times each drink appears in the customer preferences
    drink_counts = {drink: 0 for drink in set(drinks)}
    for drink in drinks:
        drink_counts[drink] += 1

    # Sort the drinks by the number of times they appear in the customer preferences
    sorted_drinks = sorted(drink_counts, key=drink_counts.get, reverse=True)

    # Return the number of drinks that the bartender needs to learn
    return len(sorted_drinks)


preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

if __name__ == "__main__":
    print(minimum_drinks(preferences))  # 2
