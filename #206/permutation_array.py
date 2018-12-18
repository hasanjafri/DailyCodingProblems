def permutate_array(lst, perm):
    permutated_array = []
    for num in perm:
        permutated_array.append(lst[num])

    return permutated_array

if __name__ == "__main__":
    print(permutate_array(["a", "b", "c"], [2, 1, 0]))