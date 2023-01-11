def kaprekar_steps(n):
    count = 0
    while n != 6174:
        n = int(''.join(sorted(str(n), reverse=True))) - int(''.join(sorted(str(n))))
        count += 1
    return count

if __name__ == '__main__':
    print(kaprekar_steps(1234))