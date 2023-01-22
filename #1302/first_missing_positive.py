def first_missing_positive(nums):
    n = len(nums)

    # Move all non-positive numbers to the left side of the array
    for i in range(n):
        if nums[i] <= 0:
            nums[i], nums[0] = nums[0], nums[i]
            i -= 1

    # Mark the presence of positive integers by making the number at the corresponding index negative
    for i in range(1, n):
        num = abs(nums[i])
        if 0 < num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    # Find the first index with a positive number
    for i in range(1, n):
        if nums[i] > 0:
            return i + 1

    return n + 1

if __name__ == '__main__':
    print(first_missing_positive([3, 4, -1, 1]))  # Output 2
    print(first_missing_positive([1, 2, 0]))  # Output 3
