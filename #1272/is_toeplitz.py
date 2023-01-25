def is_toeplitz(matrix):
    # Iterate through each element of the matrix, starting from the second row and second column
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            # Check if the current element is equal to the element above and to the left of it
            if matrix[i][j] != matrix[i-1][j-1]:
                return False
    return True

matrix = [[1, 2, 3, 4, 8],
          [5, 1, 2, 3, 4],
          [4, 5, 1, 2, 3],
          [7, 4, 5, 1, 2]]

if __name__ == '__main__':
    print(is_toeplitz(matrix)) # True