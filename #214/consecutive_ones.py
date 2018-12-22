import re

def consecutive_ones(num):
    binary_str = '{0:08b}'.format(num)
    return max(len(char) for char in re.findall(r'1+', binary_str))

if __name__ == "__main__":
    print(consecutive_ones(156))