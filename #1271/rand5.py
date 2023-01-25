import random
def rand7():
    return random.randint(1,7)

def rand5():
    # Call rand7() and take the remainder when divided by 5
    # Add 1 to the result to shift the range from 0-4 to 1-5
    return rand7() % 5 + 1

if __name__ == '__main__':
    print('Rolling 5-sided die...')
    print(rand5())