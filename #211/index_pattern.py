import re

def index_pattern(strInput, pattern):
    return [i.start() for i in re.finditer(pattern, strInput)]

if __name__ == "__main__":
    print(index_pattern('abracadabra', 'abr'))