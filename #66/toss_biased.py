import random

def toss_biased():
    return random.triangular(0, 1)

if __name__ == "__main__":
    print(toss_biased())