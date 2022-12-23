def swap_bits(x):
    # Use a bitmask to isolate the even bits and shift them right by one position
    even_bits = (x & 0b10101010) >> 1
    # Use a bitmask to isolate the odd bits and shift them left by one position
    odd_bits = (x & 0b01010101) << 1
    # Combine the even and odd bits using the bitwise OR operator |
    return even_bits | odd_bits


if __name__ == '__main__':
    print(bin(swap_bits(0b10101010)))  # Output: 0b01010101
    print(bin(swap_bits(0b11100010)))  # Output: 0b11010001
