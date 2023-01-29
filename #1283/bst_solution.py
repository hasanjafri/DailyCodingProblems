class BSTNode:
    def __init__(self, val, count=1, left=None, right=None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right


class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []

        result = [0] * len(nums)
        root = None

        for i in range(len(nums) - 1, -1, -1):
            root, result[i] = self.insert(nums[i], root, 0)

        return result

    def insert(self, num, node, smaller):
        if not node:
            return BSTNode(num), smaller

        if num <= node.val:
            node.count += 1
            node.left, smaller = self.insert(num, node.left, smaller)
        else:
            smaller += node.count
            node.right, smaller = self.insert(num, node.right, smaller + 1)

        return node, smaller


if __name__ == "__main__":
    print(Solution().countSmaller([3, 4, 9, 6, 1]))  # Outputs [1, 1, 2, 1, 0]
