numerals = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def roman_numeral_converter(rn):
    value = 0
    rnLength = len(rn)
    for char in range(rnLength):
        if (char+1) == rnLength:
            value += numerals[rn[char]]
            print(value)
        else:
            if numerals[rn[char]] < numerals[rn[char+1]]:
                value += (numerals[rn[char+1]] - numerals[rn[char]])
                print(value)
            else:
                value += numerals[rn[char]]
                print(value)
    return value

if __name__ == "__main__":
    print(roman_numeral_converter('XIV'))
    print(roman_numeral_converter('CCXLV'))