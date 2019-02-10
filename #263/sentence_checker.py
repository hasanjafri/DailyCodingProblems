import re

allowed_characters = [
    'a', 'A',
    'b', 'B',
    'c', 'C',
    'd', 'D',
    'e', 'E',
    'f', 'F',
    'g', 'G',
    'h', 'H',
    'i', 'I',
    'j', 'J',
    'k', 'K',
    'l', 'L',
    'm', 'M',
    'n', 'N',
    'o', 'O',
    'p', 'P',
    'q', 'Q',
    'r', 'R',
    's', 'S',
    't', 'T',
    'u', 'U',
    'v', 'V',
    'w', 'W',
    'x', 'X',
    'y', 'Y',
    'z', 'Z',
    ',', ';',
    ':'
]

terminals = [
    '.', '?',
    '!', '‽'
]

def sentence_checker(sentence):
    for x in re.findall(r'\s+', sentence):
        if x != ' ':
            return("Invalid Sentence1")
    
    for char in sentence[1:-1]:
        if char not in allowed_characters[:52:2] and char not in terminals and char != ' ':
            return("Invalid Sentence2")

    if not sentence[0].isupper():
        return("Invalid Sentence3")
    if not sentence[-1] in terminals:
        return("Invalid Sentence4")
    elif not sentence[-2] in allowed_characters[:52]:
        return("Invalid Sentence5")
    else:
        return(sentence)

if __name__ == "__main__":
    print(sentence_checker("How are your balls?"))