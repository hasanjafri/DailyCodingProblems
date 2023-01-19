def next_biggest(n):
    c = n
    c0, c1 = 0, 0
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    p = c0 + c1
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1-1))-1
    return n


if __name__ == '__main__':
    print(next_biggest(6))