def sort_RGB(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == "R":
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == "G":
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


if __name__ == "__main__":
    colors = ["G", "B", "R", "R", "B", "R", "G"]
    print(sort_RGB(colors))  # Output: ['R', 'R', 'R', 'G', 'G', 'B', 'B']
