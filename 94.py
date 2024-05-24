# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.list = []

    def inorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            self.list.append(root.val)
            self.inorderTraversal(root.right)
        return self.list

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.inorderTraversal(root))