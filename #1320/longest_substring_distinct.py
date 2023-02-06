def longest_substring_with_k_distinct_characters(s, k):
    char_count = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        char = s[end]
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

        while len(char_count) > k:
            char_to_remove = s[start]
            char_count[char_to_remove] -= 1
            if char_count[char_to_remove] == 0:
                del char_count[char_to_remove]
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


if __name__ == "__main__":
    print(longest_substring_with_k_distinct_characters("araaci", 2))  # Outputs 4
    print(longest_substring_with_k_distinct_characters("araaci", 1))  # Outputs 2
    print(longest_substring_with_k_distinct_characters("cbbebi", 3))  # Outputs 5
