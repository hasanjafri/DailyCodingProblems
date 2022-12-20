def kmp_match(text, pattern):
    # Preprocess the pattern to create the partial match table
    partial_match = [0] * (len(pattern) + 1)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = partial_match[j]
        if pattern[j] == pattern[i]:
            j += 1
        partial_match[i + 1] = j

    # Search for the pattern in the text
    i = 0
    j = 0
    while i < len(text):
        while j > 0 and pattern[j] != text[i]:
            j = partial_match[j]
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            return i - (j - 1)
        i += 1

    # Return False if the pattern is not found
    return False


if __name__ == '__main__':
    print(kmp_match('abcdefghijklmnopqrstuvwxyz', 'def'))  # 3
    print(kmp_match('abcdefghijklmnopqrstuvwxyz', 'xyz'))  # 23
    print(kmp_match('abcdefghijklmnopqrstuvwxyz', 'abc'))  # 0
    print(kmp_match('abcdefghijklmnopqrstuvwxyz', 'klm'))  # 10
    print(kmp_match('abcdefghijklmnopqrstuvwxyz', 'wxy'))  # 22
    print(kmp_match('abcdefghijklmnopqrstuvwxyz', 'zzz'))  # False
