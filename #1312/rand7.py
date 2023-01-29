import random

def rand5():
    return random.randint(1, 5)

def rand7():
    result = (rand5() - 1) * 5 + rand5() - 1
    if result < 21:
        return result % 7 + 1
    return rand7()

if __name__ == '__main__':
    for i in range(10):
        print(rand7())