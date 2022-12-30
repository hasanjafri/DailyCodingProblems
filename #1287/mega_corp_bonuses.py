def mega_corp_bonuses(arr):
    # Sort the array in non-ascending order
    arr.sort(reverse=True)
    # Initialize the bonus array with the same number of elements as arr
    bonuses = [0] * len(arr)
    # Assign the first bonus
    bonuses[-1] = 1
    # Iterate through the array in reverse
    for i in range(len(arr) - 2, -1, -1):
        # If the current employee has more lines of code than the previous one,
        # their bonus should be one greater than the previous employee's bonus
        if arr[i] > arr[i + 1]:
            bonuses[i] = bonuses[i + 1] + 1
        # Otherwise, their bonus should be the same as the previous employee's bonus
        else:
            bonuses[i] = bonuses[i + 1]
    # Reverse the bonuses array to get the correct order
    bonuses.reverse()
    return bonuses


if __name__ == '__main__':
    # should print [1, 2, 3, 4, 2, 1]
    print(mega_corp_bonuses([10, 40, 200, 1000, 60, 30]))
