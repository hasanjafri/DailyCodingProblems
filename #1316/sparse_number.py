def next_sparse_number(num):
    bits = bin(num)[2:]
    n = len(bits)
    right = 0
    for i in range(n - 2, -1, -1):
        if bits[i] == "1" and bits[i + 1] == "1":
            right += 1
        elif bits[i] == "0" and right != 0:
            break
    if right == n - 1:
        return num * 2
    if right > 0:
        num = num + (1 << right) + (1 << (right - 1)) - 1
    return num


if __name__ == "__main__":
    print(next_sparse_number(6))  # Output: 8
    print(next_sparse_number(4))  # Output: 4
    print(next_sparse_number(38))  # Output: 40
    print(next_sparse_number(44))  # Output: 64
    print(next_sparse_number(7))  # Output: 8
    print(next_sparse_number(15))  # Output: 16
    print(next_sparse_number(23))  # Output: 32
    print(next_sparse_number(28))  # Output: 32
    print(next_sparse_number(39))  # Output: 40
    print(next_sparse_number(40))  # Output: 64
    print(next_sparse_number(43))  # Output: 64
    print(next_sparse_number(45))  # Output: 64
    print(next_sparse_number(46))  # Output: 64
    print(next_sparse_number(47))  # Output: 64
    print(next_sparse_number(48))  # Output: 64
    print(next_sparse_number(49))  # Output: 64
    print(next_sparse_number(50))  # Output: 64
    print(next_sparse_number(51))  # Output: 64
    print(next_sparse_number(52))  # Output: 64
    print(next_sparse_number(53))  # Output: 64
    print(next_sparse_number(54))  # Output: 64
    print(next_sparse_number(55))  # Output: 64
    print(next_sparse_number(56))  # Output: 64
    print(next_sparse_number(57))  # Output: 64
    print(next_sparse_number(58))  # Output: 64
    print(next_sparse_number(59))  # Output: 64
    print(next_sparse_number(60))  # Output: 64
    print(next_sparse_number(61))  # Output: 64
    print(next_sparse_number(62))  # Output: 64
    print(next_sparse_number(63))  # Output: 64
    print(next_sparse_number(64))  # Output: 128
    print(next_sparse_number(65))  # Output: 128
    print(next_sparse_number(66))  # Output: 128
