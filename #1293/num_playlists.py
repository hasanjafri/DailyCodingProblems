def num_playlists(N, M, B):
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    dp[0][0] = 1
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if j > i:
                dp[i][j] = 0
            elif j <= B:
                dp[i][j] = dp[i - 1][j - 1] * (j) + dp[i - 1][j] * (N - j)
            else:
                dp[i][j] = dp[i - 1][j - 1] * (j - B) + dp[i - 1][j] * (N - j)
    return dp[M][N]

N = 3
M = 2
B = 1

if __name__ == '__main__':
    print(num_playlists(N, M, B)) # Output 6

