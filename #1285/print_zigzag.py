def print_zigzag(s: str, k: int):
    lines = []
    current_line = 0
    direction = 1
    for c in s:
        if current_line == k:
            current_line = k - 2
            direction = -1
        elif current_line == -1:
            current_line = 1
            direction = 1
        if len(lines) <= current_line:
            lines.append(c)
        else:
            lines[current_line] += c
        current_line += direction
    for i in range(k):
        for j, line in enumerate(lines):
            if j == i:
                print(line, end='')
            else:
                print(' ' * len(lines[i]), end='')
        print()


if __name__ == '__main__':
    print_zigzag("thisisazigzag", 4)
    # print_zigzag("thisisazigzag", 5)
