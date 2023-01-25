def kaprekar_steps(x):
    steps = 0
    while x != 6174:
        x = int("".join(sorted(str(x), reverse=True))) - int("".join(sorted(str(x))))
        steps += 1
    return steps

if __name__ == '__main__':
    print(kaprekar_steps(1234)) # 3