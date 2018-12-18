def permutate_array(lst, perm):
    return [lst[num] for num in perm]

if __name__ == "__main__":
    print(permutate_array(["a", "b", "c"], [2, 1, 0]))