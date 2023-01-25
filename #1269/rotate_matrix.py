def rotate_matrix(matrix):
    n = len(matrix)
    # Initialize the result matrix with the same dimensions as the input
    result = [[0 for _ in range(n)] for _ in range(n)]
    # Iterate through each element of the input matrix
    for i in range(n):
        for j in range(n):
            # Rotate the element by 90 degrees clockwise
            # and assign it to the corresponding position in the result matrix
            result[j][n-1-i] = matrix[i][j]
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

if __name__ == '__main__':
    rotated_matrix = rotate_matrix(matrix)
    print(rotated_matrix)