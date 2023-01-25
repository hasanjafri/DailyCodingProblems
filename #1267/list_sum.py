class ListSum:
    def __init__(self, L):
        self.L = L
        self.sums = [0] * (len(L) + 1)
        # Pre-processing step:
        # Calculate prefix sums for all elements in L
        for i in range(1, len(L) + 1):
            self.sums[i] = self.sums[i-1] + L[i-1]
        
    def sum(self, i, j):
        # Return the sum of the sublist L[i:j]
        return self.sums[j] - self.sums[i]

L = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    list_sum = ListSum(L)
    print(list_sum.sum(1,3)) # 5
