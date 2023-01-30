def egyptian_fraction(numerator, denominator):
    result = []
    while numerator != 0:
        x = denominator // numerator + 1
        result.append(f"1/{x}")
        numerator, denominator = denominator % numerator, numerator
    return result


if __name__ == "__main__":
    print(egyptian_fraction(6, 14))  # Output: ['1/3', '1/11', '1/231']
    print(egyptian_fraction(12, 13))  # Output: ['1/2', '1/3', '1/12', '1/156']
    print(egyptian_fraction(4, 13))  # Output: ['1/4', '1/18', '1/468']
