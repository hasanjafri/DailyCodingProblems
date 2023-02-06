def roman_to_decimal(s):
    values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    result = 0
    prev = 0
    for i in range(len(s) - 1, -1, -1):
        current = values[s[i]]
        if prev > current:
            result -= current
        else:
            result += current
        prev = current

    return result


if __name__ == "__main__":
    print(roman_to_decimal("MCMIV"))  # Outputs 1904
    print(roman_to_decimal("MMVIII"))  # Outputs 2008
    print(roman_to_decimal("MDCLXVI"))  # Outputs 1666
    print(roman_to_decimal("XIV"))  # Outputs 14
