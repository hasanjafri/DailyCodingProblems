def longest_palindromic_substring(s):
  n = len(s)
  dp = [[False] * n for _ in range(n)]
  for i in range(n):
    dp[i][i] = True

  longest_substring = s[0]
  for length in range(2, n+1):
    for i in range(n-length+1):
      j = i + length - 1
      if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
        dp[i][j] = True
        if length > len(longest_substring):
          longest_substring = s[i:j+1]

  return longest_substring

if __name__ == "__main__":
    print(longest_palindromic_substring('aabcdcb'))  # 'bcdcb'
    print(longest_palindromic_substring('bananas'))  # 'anana'
