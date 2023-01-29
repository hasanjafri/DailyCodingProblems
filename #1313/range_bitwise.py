def range_bitwise(m, n):
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return n << i

if __name__ == '__main__':
    print(range_bitwise(5, 7)) # Outputs 4
    print(range_bitwise(0, 1)) # Outputs 0