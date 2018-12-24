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
    indexes = set([])
    
    for char in (x for x in range(rnLength) if not x in indexes):
        if (char+1) == rnLength:
            value += numerals[rn[char]]
        else:
            if numerals[rn[char]] < numerals[rn[char+1]]:
                value += (numerals[rn[char+1]] - numerals[rn[char]])
                indexes.add(char)
                indexes.add(char+1)
            else:
                value += numerals[rn[char]]
                indexes.add(char)
    return value

if __name__ == "__main__":
    print(roman_numeral_converter('XIV'))
    print(roman_numeral_converter('CCXLV'))