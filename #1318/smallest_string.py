def smallest_string(s, k):
    n = len(s)
    smallest = s
    for i in range(n):
        s = s[1:] + s[0]
        if s < smallest:
            smallest = s
        k -= 1
        if k == 0:
            break
    return smallest

if __name__ == '__main__':
    print(smallest_string('daily', 1)) # Output: ailyd