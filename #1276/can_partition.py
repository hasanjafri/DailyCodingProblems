def can_partition(multiset):
  total = sum(multiset)
  if total % 2 == 1:
    return False

  n = len(multiset)
  target = total // 2
  dp = [[False] * (target + 1) for _ in range(n + 1)]
  dp[0][0] = True
  for i in range(1, n + 1):
    for j in range(target + 1):
      dp[i][j] = dp[i-1][j]
      if j >= multiset[i-1]:
        dp[i][j] |= dp[i-1][j-multiset[i-1]]
  return dp[n][target]

if __name__ == '__main__':
    print(can_partition([15, 5, 20, 10, 35, 15, 10]))  # True
    print(can_partition([15, 5, 20, 10, 35]))  # False