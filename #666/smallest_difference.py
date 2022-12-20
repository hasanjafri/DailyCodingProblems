def smallest_difference(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)

    # Initialize a 2D array to store the results of subproblems
    dp = [[False] * (total_sum + 1) for _ in range(len(nums) + 1)]

    # Set the first column to True, since it is always possible to get a sum of 0 by not selecting any elements
    for i in range(len(nums) + 1):
        dp[i][0] = True

    # Iterate through the array and the possible sums
    for i in range(1, len(nums) + 1):
        for j in range(1, total_sum + 1):
            # Set the current cell to the value of the cell above (not selecting the current element)
            dp[i][j] = dp[i - 1][j]

            # If it is possible to get the current sum by selecting the current element,
            # set the current cell to True
            if nums[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - nums[i - 1]]

    # Find the smallest possible difference by iterating through the array and finding the first
    # sum that can be obtained by selecting a subset of the elements
    for i in range(total_sum // 2, -1, -1):
        if dp[len(nums)][i]:
            return total_sum - 2 * i


if __name__ == '__main__':
    print(smallest_difference([5, 10, 15, 20, 25]))  # 5
    print(smallest_difference([1, 2, 3, 4, 5]))  # 1
    print(smallest_difference([1, 3, 5, 7, 9]))  # 2
    print(smallest_difference([2, 4, 6, 8, 10]))  # 1
    print(smallest_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 1
