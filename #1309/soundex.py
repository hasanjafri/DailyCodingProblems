import re


def soundex(name):
    name = name.upper()
    first_letter = name[0]
    # remove consecutive consonants with the same sound
    name = re.sub(r'([bcdfghjklmnpqrstvwxyz])\1+', r'\1', name[1:])
    # remove vowels, including y, w, and h
    name = re.sub(r'[aeiouyhw]', '', name)
    # replace consonants with digits
    name = re.sub(r'[bfpv]', '1', name)
    name = re.sub(r'[cgjkqsxz]', '2', name)
    name = re.sub(r'[dt]', '3', name)
    name = re.sub(r'[l]', '4', name)
    name = re.sub(r'[mn]', '5', name)
    name = re.sub(r'[r]', '6', name)
    # append zeros until you have three numbers
    name = name[:3].ljust(3, '0')
    return first_letter + name


if __name__ == '__main__':
    print(soundex('Robert'))
    print(soundex('Rupert'))
    print(soundex('Rubin'))
    print(soundex('Ashcraft'))
    print(soundex('Ashcroft'))
    print(soundex('Tymczak'))
    print(soundex('Pfister'))
