def minimum_remaining_quxes(arr):
    red, green, blue = 0, 0, 0
    for qux in arr:
        if qux == 'R':
            red += 1
        elif qux == 'G':
            green += 1
        elif qux == 'B':
            blue += 1
    return (2 - (red % 2 + green % 2 + blue % 2))

quxes = ['R', 'G', 'B', 'G', 'B']

if __name__ == '__main__':
    print(minimum_remaining_quxes(quxes))
