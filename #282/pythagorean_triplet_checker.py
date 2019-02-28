def pythagorean_triplet_checker(triplet_array):
    arr_len = len(triplet_array)
    for i in range(arr_len):
        triplet_array[i] = triplet_array[i] ** 2

    triplet_array.sort()

    for val in range(arr_len-1, 1, -1):
        j = 0
        k = val - 1

        while (j < k):
            if (triplet_array[j] + triplet_array[k] == triplet_array[val]):
                return True
            else:
                if (triplet_array[j] + triplet_array[k] < triplet_array[val]):
                    j += 1
                else:
                    k -= 1
    
    return False

if __name__ == "__main__":
    print(pythagorean_triplet_checker([3, 4, 5]))