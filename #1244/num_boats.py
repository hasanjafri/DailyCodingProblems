def num_boats(people, limit):
    people.sort(reverse=True)
    i, j = 0, len(people) - 1
    num_boats = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        num_boats += 1
    return num_boats


if __name__ == "__main__":
    population = [100, 200, 150, 80]
    limit = 200
    print(num_boats(population, limit))  # Output: 3
