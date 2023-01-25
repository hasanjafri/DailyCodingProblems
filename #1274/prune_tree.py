class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def prune_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    return root

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(0)
    root.right.left.left = TreeNode(0)
    root.right.left.right = TreeNode(0)

    prune_tree(root)
