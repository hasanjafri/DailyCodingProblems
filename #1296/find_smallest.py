def find_smallest(arr):
    n = len(arr)
    res = 1 # Initialize result
    for i in range(n):
        if arr[i] <= res: # If the current element is less than or equal to res, update res
            res = res + arr[i]
        else: # The current element is greater than res, the result is greater than res
            break
    return res

arr = [1, 2, 3, 10]

if __name__ == '__main__':
    print(find_smallest(arr)) # Output 7
