def find_anagrams(W, S):
    from collections import Counter

    # Create a Counter object for the word W
    W_count = Counter(W)
    n, m = len(S), len(W)
    # Create a list to store the starting indices of anagrams
    result = []
    # Create a Counter object for the first m characters of S
    S_count = Counter(S[:m])
    for i in range(n-m+1):
        if S_count == W_count:
            result.append(i)
        # Update the Counter object for the next m characters of S
        S_count[S[i]] -= 1
        if S_count[S[i]] == 0:
            del S_count[S[i]]
        if i+m < n:
            S_count[S[i+m]] += 1
    return result

W = "ab"
S = "abxaba"

if __name__ == '__main__':
    print(find_anagrams(W, S)) # [0, 3, 4]
