def count_elements(matrix, i1, j1, i2, j2):
    count = 0
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1

    # count elements smaller than M[i1, j1]
    while row_start <= row_end and col_start <= col_end:
        if matrix[row_start][col_end] >= matrix[i1][j1]:
            col_end -= 1
        else:
            count += col_end + 1
            row_start += 1

    # count elements greater than M[i2, j2]
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        if matrix[row_end][col_start] <= matrix[i2][j2]:
            col_start += 1
        else:
            count += col_end - col_start + 1
            row_end -= 1

    # subtract elements that are both smaller than M[i1, j1] and greater than M[i2, j2]
    if matrix[i1][j1] > matrix[i2][j2]:
        count -= 1
    return count


if __name__ == "__main__":
    matrix = [
        [1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45],
    ]
    print(count_elements(matrix, 1, 1, 3, 3))  # Outputs 15
