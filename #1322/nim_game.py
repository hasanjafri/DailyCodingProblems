def nim_game(heap):
    nim_sum = heap[0]
    for i in range(1, len(heap)):
        nim_sum = nim_sum ^ heap[i]
    return nim_sum != 0

if __name__ == "__main__":
    print(nim_game([1, 2, 3]))  # Outputs True
    print(nim_game([1, 2, 4]))  # Outputs False