def look_and_say(n):
    result = "1"
    for _ in range(n - 1):
        next_result = ""
        i = 0
        while i < len(result):
            count = 1
            while i + 1 < len(result) and result[i] == result[i + 1]:
                i += 1
                count += 1
            next_result += str(count) + result[i]
            i += 1
        result = next_result
    return result


if __name__ == "__main__":
    print(look_and_say(1))  # Output: 1
    print(look_and_say(2))  # Output: 11
    print(look_and_say(3))  # Output: 21
    print(look_and_say(4))  # Output: 1211
    print(look_and_say(5))  # Output: 111221
    print(look_and_say(6))  # Output: 312211
    print(look_and_say(7))  # Output: 13112221
    print(look_and_say(8))  # Output: 1113213211
    print(look_and_say(9))  # Output: 31131211131221
    print(look_and_say(10))  # Output: 13211311123113112211
